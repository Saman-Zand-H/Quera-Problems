from numbers import Number


class Chain:
    def __init__(self, arg):
        self.args = [arg]
        self.type = type(arg)
        if not isinstance(arg, (Number, str)):
            raise Exception("invalid operation")
        if isinstance(arg, Number):
            self.type = Number
        self._out()
        
    def _validate_arg(self, arg):
        if not isinstance(arg, self.type):
            raise Exception("invalid operation")
        
    def _check(self):
        is_str = isinstance(self.args[0], str)
        is_number = isinstance(self.args[0], Number)
        is_homo = is_str or is_number
        if not is_homo:
            return 0
        return str if is_str else Number
    
    def _handle_number(self):
        self.results = sum(self.args)
        if isinstance(self.results, float):
            self.results = (int(self.results) 
                            if self.results.is_integer() 
                            else float(f"{self.results:.10f}"))
            
    def _handle_str(self):
        self.results = " ".join(self.args).strip()
        
    def _out(self):
        check = self._check()
        if check:
            (
                self._handle_str()
                if check is str 
                else self._handle_number()
            )
            return 
        raise Exception("invalid operation")
            
    def __call__(self, arg):
        self._validate_arg(arg)
        self.args.append(arg)
        self._out()
        return self
        
    def __str__(self):
        return f"{self.results}"
        
    def __repr__(self):
        return f"{self.results}"
    
    def __eq__(self, o: object) -> bool:
        return self.results == o
    