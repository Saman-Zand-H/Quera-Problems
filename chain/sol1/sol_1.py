class Chain:
    def __init__(self, arg, *args):
        self.args = [arg]
        self.args.extend(args)
        self.prepare_output()
        
    def __eq__(self, val):
        return self.result == val
        
    def __str__(self):
        return self.result
    
    def __repr__(self):
        return f"Chain({self.args})"
    
    def prepare_output(self):
        self._check_types()
        if isinstance(self.args[0], str):
            self.result = " ".join(self.args)
        elif (isinstance(self.args[0], int) 
              or isinstance(self.args[0], float)):
            self.result = sum(self.args)
        
        
    def _check_types(self):
        if (
            self.args 
            and all([isinstance(item, type(self.args[0])) 
                     for item in self.args])
        ):
            return True
        raise Exception("invalid operation")
        
    def __call__(self, arg):
        self.args.append(arg)
        self.prepare_output()
        return self
        
        
if __name__ == "__main__":
    print(Chain("hello")("there")(1))
        