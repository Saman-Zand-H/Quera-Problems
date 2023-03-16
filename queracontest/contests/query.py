from django.contrib.auth import get_user_model
from django.db.models import Max, Count, F, Q, Sum, Subquery, OuterRef
from django.shortcuts import get_object_or_404
from functools import wraps

from problems.models import Submission, Problem
from .models import Contest

User = get_user_model()


def queryset_exists(func):
    @wraps(func)
    def wrapper(contest_id):
        contest_qs = Contest.objects.filter(id=contest_id)
        if contest_qs.exists():
            return func(contest_id)
        return contest_qs
    return wrapper    


@queryset_exists
def list_problems(contest_id):
    return (
        Contest
        .objects
        .get(id=contest_id)
        .problems
        .all()
    )


@queryset_exists
def list_users(contest_id):
    return (
        Contest
        .objects
        .get(id=contest_id)
        .participants
        .all()
    )
    

@queryset_exists
def list_submissions(contest_id):
    return (
        Submission
        .objects
        .filter(
            problem__contest__id=contest_id)
        .order_by("-submitted_time")
    )


def list_problem_submissions(contest_id, problem_id):
    return (
        Submission
        .objects
        .filter(
            Q(problem__id=problem_id)
            & Q(problem__contest__id=contest_id)
        )
        .order_by("-submitted_time")
    )


def list_user_submissions(contest_id, user_id):
    return (
        Submission
        .objects
        .filter(
            Q(problem__contest__id=contest_id)
            & Q(participant__id=user_id)
        )
        .order_by("-submitted_time")
    )


def list_problem_user_submissions(contest_id, user_id, problem_id):
    return (
        Submission
        .objects
        .filter(
            Q(problem__contest__id=contest_id)
            & Q(participant__id=user_id)
            & Q(problem__id=problem_id)
        )
        .order_by("-submitted_time")
    )


def list_users_solved_problem(contest_id, problem_id):
    return (
        User
        .objects
        .filter(
            Q(submissions__problem__contest__id=contest_id)
            & Q(submissions__problem__id=problem_id)
            & Q(submissions__problem__score=F("submissions__score"))
        )
        .order_by("-submissions__submitted_time")
        .distinct()
    )


def user_score(contest_id, user_id):
    problems = Problem.objects.filter(
        Q(contest__id=contest_id)
        & Q(submissions__participant__id=user_id)
    ).distinct()
    scores = []
    for problem in problems:
        scores.append(
            problem
            .submissions
            .filter(participant_id=user_id)
            .aggregate(max_score=Max("score"))["max_score"]
        )
    return sum(scores)


def list_final_submissions(contest_id):
    subquery = Subquery(
        Submission.objects.filter(
            Q(participant_id=OuterRef("participant_id"))
            & Q(problem_id=OuterRef("problem_id"))
        ).values("score").order_by("-score")[:1]
    )
    return (
        Submission
        .objects
        .filter(
            Q(problem__contest__id=contest_id)
            & Q(score=subquery)
        )
        .values("problem_id")
        .distinct()
        .order_by("participant_id")
        .values("participant_id", "problem_id")
        .annotate(score__max=F("score"))
    )
