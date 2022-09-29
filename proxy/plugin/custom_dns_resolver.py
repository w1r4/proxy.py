# -*- coding: utf-8 -*-
"""
    proxy.py
    ~~~~~~~~
    ⚡⚡⚡ Fast, Lightweight, Pluggable, TLS interception capable proxy server focused on
    Network monitoring, controls & Application development, testing, debugging.

    :copyright: (c) 2013-present by Abhinav Singh and contributors.
    :license: BSD, see LICENSE for more details.

    .. spelling::

       dns
    using dnspython module dont forget to install first   
"""
import socket
import dns.resolver
from typing import Tuple, Optional

from ..http.proxy import HttpProxyBasePlugin
from ..common.types import HostPort


class CustomDnsResolverPlugin(HttpProxyBasePlugin):
    """This plugin demonstrate how to use your own custom DNS resolver."""

    def resolve_dns(self, host: str, port: int) -> Tuple[Optional[str], Optional[HostPort]]:
        """Here we are using in-built python resolver for demonstration.

        Ideally you would like to query your custom DNS server or even
        use :term:`DoH` to make real sense out of this plugin.

        The second parameter returned is None.  Return a 2-tuple to
        configure underlying interface to use for connection to the
        upstream server.
        """
        try:
            """return socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)[0][4][0], None
        except socket.gaierror:
            # Ideally we can also thrown HttpRequestRejected or HttpProtocolException here
            # Returning None simply fallback to core generated exceptions.
            return None, None
"""
            lo_resolver = dns.resolver.Resolver()
            
            """This is my dns resolver"""
            lo_resolver.nameservers = ['1.1.1.1']

            lt_answers = my_resolver.query( host )
            lt_nameservers = [ns.to_text() for ns in lt_answers]
            if len(lt_nameservers) == 0:
                return None, None
            # TODO: Utilize TTL to cache response locally
            # instead of making a DNS query repeatedly for the same host.
            return lt_nameservers[0], None
        except socket.gaierror:
            return None, None        
