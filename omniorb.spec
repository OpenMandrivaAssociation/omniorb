%define version		4.1.4
%define release		%mkrel 3
%define name		omniorb
%define lib_name_orig	lib%{name}
%define lib_major	4
%define lib_name	%mklibname %{name} %{lib_major}
%define develname 	%mklibname -d %{name}
%{expand:%%define py_ver %(python -V 2>&1| awk '{print $2}'|cut -d. -f1-2)}
%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"
%{?!mdkversion: %define notmdk 1}

# virtual (ie empty) package to enforce naming convention

Summary:	A robust high performance CORBA ORB for C++ and Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source0:	http://prdownloads.sourceforge.net/sourceforge/omniorb/omniORB-%{version}.tar.gz
Source1:	omniORB.cfg
Source2:	omninames
URL:		http://omniorb.sourceforge.net/
BuildRequires:	tcl tk
%py_requires -d
BuildRequires:	openssl-devel
%{!?notmdk:Requires(pre): rpm-helper}
%{!?notmdk:Requires(preun): rpm-helper}
Provides:	corba
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{lib_name} = %version
ExclusiveArch:	ppc i586 x86_64

Patch0:		omniORB-4.1.4-format.patch
Patch1:		omniORB-4.1.4-openssl-1.0.patch

%description
omniORB is a robust high performance CORBA ORB for C++ and Python.
It is freely available under the terms of the GNU Lesser General Public License
(for the libraries), and GNU General Public License (for the tools). omniORB
is largely CORBA 2.6 compliant.

omniORB is one of only three ORBs to have been awarded the Open Group's Open
Brand for CORBA. This means that omniORB has been tested and certified CORBA
compliant, to version 2.1 of the CORBA specification. You can find out more
about the branding program at the Open Group. 

# main package (contains *.so.[major].*, and binaries)

%package -n	%{lib_name}
Summary:	a robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Provides:	%{lib_name_orig} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with %{lib_name_orig}.

%package -n	%{develname}
Summary:	Header files and libraries needed for %{name} development
Group:		Development/C++
Requires:	%{name} = %{version}
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}omniorbpy-devel < %{version}-%{release}
Obsoletes:	%{_lib}omniorb4-devel < %{version}-%{release}
Obsoletes:	%{_lib}omniorb-devel < %{version}-%{release}

%description -n	%{develname}
This package includes the header files and libraries needed for
developing programs using %{name}.

# docs and examples are in a separate package

%package -n	%{name}-doc
Summary:	Documentation for omniORB
Group:		Development/C++
Requires:	%{name} = %{version}
Provides:	%{lib_name_orig}-doc
Obsoletes:	%{lib_name_orig}-doc
Obsoletes:	libomniorbpy-doc < %{version}-%{release}

%description -n	%{name}-doc
This package includes developers doc including examples.


%package -n python-omniidl
Group:		Development/Python
Summary:	OmniOrb IDL compiler
Conflicts:	%{lib_name}-devel < 4.1.0
Obsoletes:	%{_lib}omniorbpy2 < %{version}-%{release}

%description -n python-omniidl
OmniOrb IDL compiler

%prep 
%setup -q -n omniORB-%{version}
%patch0 -p1
%patch1 -p0

%build
%configure2_5x --with-openssl=%{_prefix}
%make

%install
[ -d %buildroot ] && rm -rf %buildroot

%makeinstall_std
###### directories #####

install -m 755 -d %buildroot%{_mandir}/{man1,man5}
install -m 755 -d %buildroot%_sysconfdir/init.d
install -m 755 -d %buildroot/var/omninames/

##### copy files #####

install -m 644 %{SOURCE1} %buildroot%_sysconfdir
install -m 755 %{SOURCE2} %buildroot%_sysconfdir/init.d/omninames

install -m 644 man/man1/* %buildroot%{_mandir}/man1/
#install -m 644 man/man5/* %buildroot%{_mandir}/man5/

mkdir -p  %buildroot/var/log/omninames
chmod 755 %buildroot/%{_includedir}/{omnithread,COS,omniORB4,omniORB4/internal}

mkdir -p %{buildroot}%{py_platsitedir}/%{name}
pushd %{buildroot}%{py_platsitedir}/%{name}
%python_compile_opt
%python_compile
#install *.pyc *.pyo %{buildroot}%{py_platsitedir}/%{name}

%clean
[ -z %buildroot ] || rm -rf %buildroot

%post
%_post_service omninames

%preun
%_preun_service omninames

%if %mdkversion < 200900
%post   -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files
%defattr (-,root,root)
%doc CREDITS ReleaseNotes.txt
%_bindir/*
%exclude %_bindir/omniidl*
%config(noreplace) %_sysconfdir/*.cfg
%_sysconfdir/init.d/*
%attr(644,root,man)  %{_mandir}/man1/*
%dir %attr(754,root,root) /var/log/omninames

%files -n %{lib_name}
%defattr (-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
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

%_libdir/pkgconfig/*

%files -n python-omniidl
%defattr(-,root,root,755)

%_bindir/omniidl*
%_datadir/idl/omniORB/*.idl
%_datadir/idl/omniORB/COS/*.idl

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
%_libdir/python%{py_ver}/site-packages/_omniidlmodule.so.*

%files -n %{name}-doc
%defattr(-,root,root)
%doc doc/*
