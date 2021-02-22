#General metrics
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
#Tosca metrics
from toscametrics.metrics.na import NA
from toscametrics.metrics.nc import NC
from toscametrics.metrics.ni import NI
from toscametrics.metrics.nif import NIF
from toscametrics.metrics.ninp import NINP
from toscametrics.metrics.ninpc import NINPC
from toscametrics.metrics.nn import NN
from toscametrics.metrics.nout import NOUT
from toscametrics.metrics.np import NP
from toscametrics.metrics.nr import NR
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
from toscametrics.metrics.ngro import NGRO
from toscametrics.metrics.npol import NPOL
from toscametrics.metrics.nf import NF
from toscametrics.metrics.td import TD
from toscametrics.metrics.au import AU
from toscametrics.metrics.nac import NAC
from toscametrics.metrics.nfunc import NFUNC
from toscametrics.metrics.noam import NOAM
from toscametrics.metrics.nop import NOP
from toscametrics.metrics.ntri import NTRI
from toscametrics.metrics.tett import TETT




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