Summary:            Zimbra components for spell package
Name:               zimbra-spell-components
Version:            2.0.0
Release:            1zimbra8.8b1ZAPPEND
License:            GPL-2
Requires:           zimbra-spell-base, zimbra-aspell-ar, zimbra-aspell-da, zimbra-aspell-de
Requires:           zimbra-aspell-en, zimbra-aspell-es, zimbra-aspell-fr, zimbra-aspell-hi
Requires:           zimbra-aspell-hu, zimbra-aspell-it, zimbra-aspell-nl, zimbra-aspell-pl
Requires:           zimbra-aspell-pt-br, zimbra-aspell-ru, zimbra-aspell-sv, zimbra-httpd >= 2.4.38-1zimbra8.7b1ZAPPEND
Requires:           zimbra-php >= 7.3.1-1zimbra8.7b3ZAPPEND, zimbra-aspell-zimbra
Packager:           Zimbra Packaging Services <packaging-devel@zimbra.com>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra spell components pulls in all the packages used by
zimbra-spell

%changelog
* Mon Mar 25 2019  Zimbra Packaging Services <packaging-devel@zimbra.com> - 2.0.0
- Updated PHP package.

%files
