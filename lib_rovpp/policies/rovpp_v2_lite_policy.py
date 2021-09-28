from copy import deepcopy

from ipaddress import ip_network

from lib_bgp_simulator import BGPPolicy, ROAValidity, Relationships

from .rovpp_v1_lite_policy import ROVPPV1LitePolicy


class ROVPPV2LitePolicy(ROVPPV1LitePolicy):

    name = "ROV++V2 Lite"

    def _policy_propagate(policy_self, self, propagate_to, send_rels, ann, as_obj):
        """Deals with blackhole propagation

        If ann is a blackhole, it must be recv from peers/providers and must
        be sent only to customers
        """

        if ann.blackhole:
            if (ann.recv_relationship in [Relationships.PEERS, Relationships.PROVIDERS]
                and propagate_to == Relationships.CUSTOMERS):

                policy_self._add_ann_to_q(self, as_obj, ann, propagate_to, send_rels)

            return True
