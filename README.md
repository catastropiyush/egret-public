# egret-public
<p align="center">
<img src="docs/visual_abstract.png" alt="Visual Abstract" width="650"/>
</p>

This repository hosts the EGRET-1 model created by Rowan. You can either use the model weights locally or run it directly on the [Rowan platform](https://labs.rowansci.com/).


The model is compatible with the ASE calculator interface. Below is an example template using the mace_off calculator from the mace-torch package:
## Example calculation
```python
import ase.io
from ase.calculators.calculator import all_changes

from mace.calculators import mace_off

atoms = read("<path_to_molecule_file>")

calculator = mace_off(model="<path_to_model/EGRET_1.model>", default_dtype="float32")

calculator.calculate(atoms, [<ASE_task_1>, <ASE_task_2>], all_changes)

print(calculator.results)
```  
