from lib_bgp_simulator import PrefixHijack, SubprefixHijack, UnnanouncedHijack

from .rovpp_ann import ROVPPAnn

class ROVPPPrefixHijack(PrefixHijack):
    """Prefix hijack with ROV++ ann class"""

    AnnCls = ROVPPAnn

class ROVPPSubprefixHijack(SubprefixHijack):
    """Subprefix hijack with ROV++ ann class"""

    AnnCls = ROVPPAnn

class ROVPPUnnanouncedPrefixHijack(UnnanouncedPrefixHijack):
    """Unannounced Prefix hijack with ROV++ ann class"""

    AnnCls = ROVPPAnn