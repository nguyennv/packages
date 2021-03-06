Summary:            Zimbra components for core package
Name:               zimbra-core-components
Version:            2.0.3
Release:            1zimbra8.8b1ZAPPEND
License:            GPL-2
Requires:           zimbra-base, zimbra-os-requirements, zimbra-perl, zimbra-pflogsumm
Requires:           zimbra-openssl >= 1.0.2t-1zimbra8.7b2ZAPPEND,zimbra-curl, zimbra-cyrus-sasl, zimbra-rsync
Requires:           zimbra-mariadb-libs >= 10.1.25-1zimbra8.7b1ZAPPEND, zimbra-openldap-client, zimbra-osl >= 2.0.0-1zimbra9.0b1ZAPPEND
Requires:           zimbra-prepflog, zimbra-tcmalloc-libs, zimbra-perl-innotop
Requires:           zimbra-openjdk >= 13.0.1-1zimbra8.8b1ZAPPEND, zimbra-openjdk-cacerts, zimbra-amavis-logwatch
Requires:           zimbra-postfix-logwatch, zimbra-rrdtool
Packager:           Zimbra Packaging Services <packaging-devel@zimbra.com>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%changelog
* Tue Apr 07 2020  Zimbra Packaging Services <packaging-devel@zimbra.com> - 2.0.3
- Update zimbra osl
* Tue Mar 31 2020  Zimbra Packaging Services <packaging-devel@zimbra.com> - 2.0.2
* Wed Dec 11 2019  Zimbra Packaging Services <packaging-devel@zimbra.com> - 2.0.1
* Wed Mar 20 2019  Zimbra Packaging Services <packaging-devel@zimbra.com> - 2.0.0
- Initial Release

%description
Zimbra core components pulls in all the packages used by
zimbra-core

%files
