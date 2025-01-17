from copy import deepcopy
from collections import defaultdict

from ipaddress import ip_network

from lib_bgp_simulator import BGPPolicy, ROAValidity, ROVPolicy, Relationships

def _new_ann_is_better(policy_self, self, deep_ann, second_ann, recv_relationship: Relationships, processed=False):
    """Assigns the priority to an announcement according to Gao Rexford"""

    best_by_relationship = policy_self._best_by_relationship(deep_ann, second_ann if processed else recv_relationship)
    if best_by_relationship is not None:
        return best_by_relationship
    else:
        best_by_hole_size = policy_self._best_by_hole_size(deep_ann, second_ann)
        if best_by_hole_size is not None:
            return best_by_hole_size
        else:
            return policy_self._best_as_path_ties(self, deep_ann, second_ann, processed=processed)

def _best_by_hole_size(policy_self, deep_ann, second_ann):
    """Best by hole size"""

    # Holes aren't counted for this prefix
    if not hasattr(deep_ann, "temp_holes"):
        return None

    if len(deep_ann.temp_holes) > len(second_ann.temp_holes):
        return True
    elif len(deep_ann.temp_holes) < len(second_ann.temp_holes):
        return False
    else:
        return None
