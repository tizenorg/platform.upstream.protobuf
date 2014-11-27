#
# spec file for package protobuf
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname 9

Name:           protobuf
Summary:        Protocol Buffers - Google's data interchange format
License:        BSD-3-Clause
Group:          System/Libraries
Version:        2.6.1
Release:        0
Url:            http://code.google.com/p/protobuf/
Source0:        http://protobuf.googlecode.com/files/%{name}-%{version}.tar.bz2

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package -n libprotobuf%{soname}
Summary:        Protocol Buffers - Google's data interchange format
Group:          System/Libraries

%description -n libprotobuf%{soname}
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package -n libprotoc%{soname}
Summary:        Protocol Buffers - Google's data interchange format
Group:          System/Libraries

%description -n libprotoc%{soname}
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package -n libprotobuf-lite%{soname}
Summary:        Protocol Buffers - Google's data interchange format
Group:          System/Libraries

%description -n libprotobuf-lite%{soname}
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/C and C++
Requires:       gcc-c++
Requires:       libprotobuf%{soname} = %version
Requires:       libprotobuf-lite%{soname}
Provides:       libprotobuf-devel = %version
Requires:       zlib-devel
BuildRequires:  pkg-config

%description devel
Development files for Google Protocol Buffers

%prep

%setup -q

%build
#
%configure --disable-static
%{__make} %{?jobs:-j%jobs}
#
%install
%makeinstall
/bin/rm %{buildroot}%{_libdir}/*.la
%__install -Dm 0644 editors/proto.vim %{buildroot}%{_datadir}/vim/site/syntax/proto.vim
%clean
rm -rf $RPM_BUILD_ROOT;

%post -n libprotobuf%{soname} -p /sbin/ldconfig

%postun -n libprotobuf%{soname} -p /sbin/ldconfig

%post -n libprotoc%{soname} -p /sbin/ldconfig

%postun -n libprotoc%{soname} -p /sbin/ldconfig

%post -n libprotobuf-lite%{soname} -p /sbin/ldconfig

%postun -n libprotobuf-lite%{soname} -p /sbin/ldconfig

%files -n libprotobuf%{soname}
%defattr(-, root, root)
%{_libdir}/libprotobuf.so.%{soname}*

%files -n libprotoc%{soname}
%defattr(-, root, root)
%{_libdir}/libprotoc.so.%{soname}*

%files -n libprotobuf-lite%{soname}
%defattr(-, root, root)
%{_libdir}/libprotobuf-lite.so.%{soname}*

%files devel
%defattr(-,root,root)
%license LICENSE
%doc CHANGES.txt CONTRIBUTORS.txt README.md
%doc examples
%{_bindir}/protoc
%{_includedir}/google
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/vim
