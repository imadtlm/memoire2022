from mp_api import MPRester
from pymatgen.electronic_structure.plotter import DosPlotter
key='sd9SslwylftsWlYlgpzJ4KSI5EU2e6Aj'
with MPRester(api_key=key) as mpr:
    #bandstructure = mpr.get_bandstructure_by_material_id('mp-1639')
    dos=mpr.get_dos_by_material_id('mp-1639')
   


element_dos = dos.get_element_dos()
tdos=dos
plotter=DosPlotter()
plotter.add_dos("DOS Total BN",tdos)
plotter.add_dos_dict(element_dos)
plotter.show(xlim=[-20, 20])
plotter.save_plot("dosBN.eps")
