# egret-public

## Example calculation
```
from mace.calculators import mace_off
from ase.build import molecule
from ase.calculators.calculator import all_changes

atoms = molecule('H2O')

calculator = mace_off(model="<path_to_model/EGRET_1.model>", default_dtype="float32")

calculator.calculate(atoms2, [<ASE_task_1>, <ASE_task_2>], all_changes)

print(calculator.results)
```  
