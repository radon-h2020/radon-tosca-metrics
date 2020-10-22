#General metrics
from toscametrics.yml.bloc import BLOC
from toscametrics.yml.cloc import CLOC
from toscametrics.yml.loc import LOC
from toscametrics.yml.dpt import DPT
from toscametrics.yml.etp import ETP
from toscametrics.yml.nco import NCO
from toscametrics.yml.nkeys import NKEYS
from toscametrics.yml.ntkn import NTKN
from toscametrics.yml.nscm import NSCM

#Tosca metrics
from toscametrics.metrics.na import NA
from toscametrics.metrics.nc import NC
from toscametrics.metrics.ni import NI
from toscametrics.metrics.nif import NIF
from toscametrics.metrics.ninp import NINP
from toscametrics.metrics.ninpc import NINPC
from toscametrics.metrics.nn import NN
from toscametrics.metrics.nnt import NNT
from toscametrics.metrics.nout import NOUT
from toscametrics.metrics.np import NP
from toscametrics.metrics.nr import NR
from toscametrics.metrics.nrt import NRT
from toscametrics.metrics.ttb import TTB
from toscametrics.metrics.cdnt import CDNT
from toscametrics.metrics.cdrt import CDRT
from toscametrics.metrics.cdat import CDAT
from toscametrics.metrics.cdct import CDCT
from toscametrics.metrics.cddt import CDDT
from toscametrics.metrics.cdgt import CDGT
from toscametrics.metrics.cdit import CDIT
from toscametrics.metrics.cdpt import CDPT
from toscametrics.metrics.nw import NW
from toscametrics.metrics.tdb import TDB
from toscametrics.metrics.nrq import NRQ
from toscametrics.metrics.nsh import NSH
from toscametrics.metrics.ncys import NCYS
from toscametrics.metrics.tob import TOB
from toscametrics.metrics.ngc import NGC
from toscametrics.metrics.ngp import NGP
from toscametrics.metrics.ngro import NGRO
from toscametrics.metrics.npol import NPOL
from toscametrics.metrics.nf import NF


general_metrics = {
    'loc'   :   LOC, 
    'bloc'  :   BLOC, 
    'cloc'  :   CLOC,
    'dpt'   :   DPT,
    'etp'   :   ETP,
    'nco'   :   NCO,
    'nkeys' :   NKEYS,
    'ntkn'  :   NTKN,
    'nscm'  :   NSCM
    }

tosca_metrics = {
    'na'    :   NA,
    #'nc'    :   NC,
    #'ni'    :   NI,
    #'nif'   :   NIF,
    'ninp'  :   NINP,
    'ninpc' :   NINPC,
    #'nn'    :   NN,
    #'nnt'   :   NNT,
    #'nout'  :   NOUT,
    #'np'    :   NP,
    #'nr'    :   NR,
    #'nrt'   :   NRT,
    #'ttb'   :   TTB,
    'cdnt'  :   CDNT,
    'cdrt'  :   CDRT,
    'cdat'  :   CDAT,
    'cdct'  :   CDCT,
    'cddt'  :   CDDT,
    'cdgt'  :   CDGT,
    'cdit'  :   CDIT,
    'cdpt'  :   CDPT,
    'nw'    :   NW,
    #'tdb'   :   TDB,
    'nrq'   :   NRQ,
    'nsh'   :   NSH,
    #'ncys'  :   NCYS,
    #'tob'   :   TOB,
    'ngc'   :   NGC,
    'ngp'   :   NGP,
    'ngro'  :   NGRO,
    'npol'  :   NPOL,
    'nf'    :   NF
    }