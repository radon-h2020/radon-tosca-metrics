#General blueprint
from toscametrics.general.lines_blank import LinesBlank
from toscametrics.general.lines_comment import LinesComment
from toscametrics.general.lines_code import LinesCode
from toscametrics.general.num_keys import NumKeys
from toscametrics.general.num_suspicious_comments import NumSuspiciousComments
from toscametrics.general.num_tokens import NumTokens
from toscametrics.general.text_entropy import TextEntropy

general_metrics = {
    'lines_code'   :   LinesCode, 
    'lines_blank'  :   LinesBlank,
    'lines_comment'  :   LinesComment,
    'num_keys'   :   NumKeys,
    'num_suspicious_comments'   :   NumSuspiciousComments,
    'num_tokens' :   NumTokens,
    'text_entropy'  :   TextEntropy,
    }

"""  
#Tosca blueprint
from toscametrics.blueprint.na import NA
from toscametrics.blueprint.nc import NC
from toscametrics.blueprint.ni import NI
from toscametrics.blueprint.nif import NIF
from toscametrics.blueprint.ninp import NINP
from toscametrics.blueprint.ninpc import NINPC
from toscametrics.blueprint.nn import NN
from toscametrics.blueprint.nout import NOUT
from toscametrics.blueprint.np import NP
from toscametrics.blueprint.nr import NR
from toscametrics.blueprint.ttb import TTB
from toscametrics.blueprint.cdnt import CDNT
from toscametrics.blueprint.cdrt import CDRT
from toscametrics.blueprint.cdat import CDAT
from toscametrics.blueprint.cdct import CDCT
from toscametrics.blueprint.cddt import CDDT
from toscametrics.blueprint.cdgt import CDGT
from toscametrics.blueprint.cdit import CDIT
from toscametrics.blueprint.cdpt import CDPT
from toscametrics.blueprint.nw import NW
from toscametrics.blueprint.tdb import TDB
from toscametrics.blueprint.nrq import NRQ
from toscametrics.blueprint.nsh import NSH
from toscametrics.blueprint.ncys import NCYS
from toscametrics.blueprint.tob import TOB
from toscametrics.blueprint.ngro import NGRO
from toscametrics.blueprint.npol import NPOL
from toscametrics.blueprint.nf import NF
from toscametrics.blueprint.td import TD
from toscametrics.blueprint.au import AU
from toscametrics.blueprint.nac import NAC
from toscametrics.blueprint.nfunc import NFUNC
from toscametrics.blueprint.noam import NOAM
from toscametrics.blueprint.nop import NOP
from toscametrics.blueprint.ntri import NTRI
from toscametrics.blueprint.tett import TETT




tosca_metrics = {
    'na'    :   NA,
    'nc'    :   NC,
    'ni'    :   NI,
    'nif'   :   NIF,
    'ninp'  :   NINP,
    'ninpc' :   NINPC,
    'nn'    :   NN,
    'nout'  :   NOUT,
    'np'    :   NP,
    'nr'    :   NR,
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
    'ncys'  :   NCYS,
    #'tob'   :   TOB,
    'ngro'  :   NGRO,
    'npol'  :   NPOL,
    'nf'    :   NF,
    #'td'    :   TD,
    'au'    :   AU,
    'nac'   :   NAC,
    'nfunc' :   NFUNC,
    'noam'  :   NOAM,
    'nop'   :   NOP,
    'ntri'  :   NTRI,
    'tett'  :   TETT
    }
""" 