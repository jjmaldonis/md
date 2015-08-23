from model import Model
import sys

def main():
    modelfile = sys.argv[1]
    m = Model(modelfile)
    extension = modelfile.split('.')[-1]
    if extension != 'dat':
        modelfile = modelfile[modelfile.rfind('/')+1:]
        modelfile = modelfile[:-4]+extension
        m.write_dat('temp.dat')
        modelfile = 'temp.dat'

    of = open("cgm_temp.in", 'w')
    of.write("""units		metal
boundary	p p p
atom_style	atomic

read_data {0}

pair_style	eam/alloy
pair_coeff	* * potentials/ZrCuAl2011.eam.alloy Zr Cu Al

thermo_style	custom step etotal fmax fnorm
thermo		1

minimize	1.0e-6 0 1000 10000
write_data  lmp_emin_exp.dat""".format(modelfile))
    of.close()

if __name__== '__main__':
    main()
