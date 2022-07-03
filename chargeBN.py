from mp_api import MPRester
from pymatgen.electronic_structure.plotter import DosPlotter
key='sd9SslwylftsWlYlgpzJ4KSI5EU2e6Aj'
from mp_api import MPRester

with MPRester(api_key=key) as mpr:
    # this will return a pymatgen Chgcar object
    charge_density = mpr.get_charge_density_from_material_id('mp-1639')
