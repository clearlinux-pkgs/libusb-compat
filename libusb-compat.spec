#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libusb-compat
Version  : 0.1.4
Release  : 4
URL      : http://sourceforge.net/projects/libusb/files/libusb-compat-0.1/libusb-compat-0.1.4/libusb-compat-0.1.4.tar.bz2
Source0  : http://sourceforge.net/projects/libusb/files/libusb-compat-0.1/libusb-compat-0.1.4/libusb-compat-0.1.4.tar.bz2
Summary  : USB access library (libusb-1.0 compat wrapper)
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: libusb-compat-bin
Requires: libusb-compat-lib
BuildRequires : pkgconfig(libusb-1.0)

%description
libusb-compat-0.1
=================
A compatibility layer allowing applications written for libusb-0.1 to work
with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell and walk
like libusb-0.1.

%package bin
Summary: bin components for the libusb-compat package.
Group: Binaries

%description bin
bin components for the libusb-compat package.


%package dev
Summary: dev components for the libusb-compat package.
Group: Development
Requires: libusb-compat-lib
Requires: libusb-compat-bin
Provides: libusb-compat-devel

%description dev
dev components for the libusb-compat package.


%package lib
Summary: lib components for the libusb-compat package.
Group: Libraries

%description lib
lib components for the libusb-compat package.


%prep
%setup -q -n libusb-compat-0.1.4

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/libusb-config

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
