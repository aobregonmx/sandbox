from pyteal import *
from beaker import *

class SaveInfo(Application):
    name = ApplicationStateValue(stack_type = TealType.bytes)
    
    @external
    def save_name(self, name_in: abi.String):
        return self.name.set(name_in.get())
    
    @external
    def get_name(self, *, output:abi.String):
        return output.set(self.name.get())