'''
NAME: Predicción de Lista de Compras
       

VERSION
        

AUTHOR: Santiago Orozco Barrera
        

DESCRIPTION
        

CATEGORY
        

USAGE

    % python programName
    

ARGUMENTS


METHOD


SEE ALSO


        
'''


# ===========================================================================
# =                            imports
# ===========================================================================

import argparse


# ===========================================================================
# =                            Command Line Options
# ===========================================================================

parser = argparse.ArgumentParser(description="Se acepta el número de invitados")
parser.add_argument("invitados", 
                    type=int,
                    default=6,
                    help ="Número de invitados")
parser.add_argument("-i", "--item"
                    type=str,
                    default=["soda", "agua", "papas", "pizza"],
                    choices=["soda", "agua", "papas", "pizza"],
                    help="El item específico que se quiere saber su cantidad")
args = parser.parse_arg()


# ===========================================================================
# =                            functions
# ===========================================================================

def c_soda(invitados): #Cantidad de soda
    return(invitados/2)

def c_papas(invitados): #Cantidad de papas
    return(invitados/3)

def c_pizza(invitados): #Cantidad de pizza
    return(invitados*3/8)

# ===========================================================================
# =                            main
# ===========================================================================


# step 1.
if args.item == "soda":
    print("Se necesitarán" + c_soda(args.invitados)+"soda(s)")

# step 2.
if args.item == "agua":
    print("Se necesitarán" + args.invitados + "botella(s) de agua")

# step 3.
if args.item == "papas":
    print("Se necesitarán" + c_papas(args.invitados)+"bolsa(s) de papas fritas")

# step 4.
if args.item == "pizza":
    print("Se necesitarán" + c_pizza(args.invitados) + "pizza(s)")
