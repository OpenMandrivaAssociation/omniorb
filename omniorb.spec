%define version 4.1.0
%define release %mkrel 1
%define name		omniorb
%define lib_name_orig	lib%{name}
%define lib_major	4
%define lib_name	%mklibname %{name} %{lib_major}
%define lib_namedevel	%mklibname -d %{name}
%{expand:%%define py_ver %(python -V 2>&1| awk '{print $2}'|cut -d. -f1-2)}

# virtual (ie empty) package to enforce naming convention

Summary:	Object Request Broker (ORB) from AT&T (CORBA 2.3)
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source0:	omniORB-%{version}.tar.gz
Source1:	omniEvents-2_4_0-src.tar.bz2
Source2:	omniORB.cfg
Source3:	omninames
URL:		http://omniorb.sourceforge.net/
BuildRequires:	perl tcl tk glibc-devel
BuildRequires:	python >= %{py_ver}
BuildRequires:	python-devel >=  %{py_ver}
BuildRequires:	openssl-devel
Provides:	corba
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{lib_name} = %version
ExclusiveArch:	ppc i586 x86_64

%description
omniORB is an Object Request Broker (ORB) from AT&T which implements
specification 2.3 of the Common Object Request Broker Architecture (CORBA).

Warning:
Before release 4.0.0, it contains OmnyORBpy, now it is a separate package.

# main package (contains *.so.[major].*, and binaries)

%package -n	%{lib_name}
Summary:	Object Request Broker (ORB) from AT&T (CORBA 2.3)
Group:		System/Libraries
Provides:	%{lib_name_orig} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with %{lib_name_orig}.

Warning:
Before release 4.0.0, it contains OmnyORBpy, now it is a separate package.

%package -n	%{lib_namedevel}
Summary:	Header files and libraries needed for %{name} development
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:  %mklibname -d %name 4

%description -n	%{lib_namedevel}
This package includes the header files and libraries needed for
developing programs using %{name}.

Warning:
Before release 4.0.0, it contains OmnyORBpy, now it is a separate package.

# docs and examples are in a separate package

%package -n	%{lib_name_orig}-doc
Summary:	Header files and libraries needed for %{name} development
Group:		Development/C++
Requires:	%{name} = %{version}
Provides:	%{lib_name_orig}-doc
Provides:	%{name}-doc
Provides:	%{lib_name_orig}3-doc
Obsoletes:	%{lib_name_orig}3-doc

%description -n	%{lib_name_orig}-doc
This package includes developers doc including examples.

Warning:
Before release 4.0.0, it contains OmnyORBpy, now it is a separate package.

%prep 
%setup -n omniORB-%{version} -q -a1

%build
%configure --with-openssl=%{_prefix}
%make

%install
[ -d %buildroot ] && rm -rf %buildroot

%makeinstall_std
###### directories #####

install -m 755 -d %buildroot%{_mandir}/{man1,man5}
install -m 755 -d %buildroot%_sysconfdir/init.d
install -m 755 -d %buildroot/var/omninames/

##### copy files #####

install -m 644 %{SOURCE2} %buildroot%_sysconfdir
install -m 755 %{SOURCE3} %buildroot%_sysconfdir/init.d/omninames

install -m 644 man/man1/* %buildroot%{_mandir}/man1/
#install -m 644 man/man5/* %buildroot%{_mandir}/man5/

mkdir -p  %buildroot/var/log/omninames
chmod 755 %buildroot/%{_includedir}/{omnithread,COS,omniORB4,omniORB4/internal}

%clean
[ -z %buildroot ] || rm -rf %buildroot

%post   -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files
%defattr (-,root,root)
%doc CREDITS ReleaseNotes.txt README.FIRST.txt README.unix
%_bindir/*
%config(noreplace) %_sysconfdir/*.cfg
%config(noreplace) %_sysconfdir/init.d/*
%attr(644,root,man)  %{_mandir}/man1/*
%dir %attr(754,root,root) /var/log/omninames

%files -n %{lib_name}
%defattr (-,root,root)
%{_libdir}/*.so.*
%_libdir/python%{py_ver}/site-packages/_omniidlmodule.so.*

%files -n %{lib_namedevel}
%defattr(-,root,root)
%doc README* 
%{_libdir}/*.a
%{_libdir}/*.so

%{_includedir}/COS/*.h
%{_includedir}/COS/*.hh
%{_includedir}/omniORB4/*.h
%{_includedir}/omniORB4/*.hh
%{_includedir}/omniORB4/internal/*.h
%{_includedir}/omniconfig.h
%{_includedir}/omnithread.h
%{_includedir}/omnithread/*

%_datadir/idl/omniORB/*.idl
%_datadir/idl/omniORB/COS/*.idl

%_libdir/pkgconfig/*
%dir %py_puresitedir/omniidl
%py_puresitedir/omniidl/*
%dir %py_puresitedir/omniidl_be
%py_puresitedir/omniidl_be/*.py*
%dir %py_puresitedir/omniidl_be/cxx
%py_puresitedir/omniidl_be/cxx/*.py
%py_puresitedir/omniidl_be/cxx/*.pyc
%py_puresitedir/omniidl_be/cxx/header
%py_puresitedir/omniidl_be/cxx/skel
%py_puresitedir/omniidl_be/cxx/dynskel
%py_puresitedir/omniidl_be/cxx/impl
%py_platsitedir/_omniidlmodule.so

%files -n %{lib_name_orig}-doc
%defattr(-,root,root)
%doc doc/*


