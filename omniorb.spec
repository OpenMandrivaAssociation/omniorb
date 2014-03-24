%define api 4
%define major 1
%define thread_major 3
%define libcos4 %mklibname COS %{api} %{major}
%define libcosdynamic4 %mklibname COSDynamic %{api} %{major}
%define libcodesets4 %mklibname omniCodeSets %{api} %{major}
%define libconmgmt4 %mklibname omniConnectionMgmt %{api} %{major}
%define libdynamic4 %mklibname omniDynamic %{api} %{major}
%define liborb4 %mklibname omniORB %{api} %{major}
%define libssl4 %mklibname omnisslTP %{api} %{major}
%define libomnithread %mklibname omnithread %{thread_major}
%define devname %mklibname %{name} -d

Summary:	A robust high performance CORBA ORB for C++ and Python
Name:		omnirb
Version:	4.1.5
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		http://omniorb.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/sourceforge/omniorb/omniORB-%{version}.tar.bz2
Source1:	omniORB.cfg
Source2:	omninames
Patch0:		omniORB-4.1.4-format.patch
Patch2:		omniORB-4.1.4-link.patch
BuildRequires:	tcl
BuildRequires:	tk
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
Requires(preun,post):	rpm-helper
Provides:	corba

%description
omniORB is a robust high performance CORBA ORB for C++ and Python.
It is freely available under the terms of the GNU Lesser General Public License
(for the libraries), and GNU General Public License (for the tools). omniORB
is largely CORBA 2.6 compliant.

omniORB is one of only three ORBs to have been awarded the Open Group's Open
Brand for CORBA. This means that omniORB has been tested and certified CORBA
compliant, to version 2.1 of the CORBA specification. You can find out more
about the branding program at the Open Group.

%files
%doc CREDITS ReleaseNotes.txt
%{_bindir}/*
%exclude %{_bindir}/omniidl*
%config(noreplace) %{_sysconfdir}/*.cfg
%{_sysconfdir}/init.d/*
%attr(644,root,man) %{_mandir}/man1/*
%dir %attr(754,root,root) /var/log/omninames

%post
%_post_service omninames

%preun
%_preun_service omninames

#----------------------------------------------------------------------------

%package -n %{libcos4}
Summary:	A robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Conflicts:	%{_lib}omniorb4 < 4.1.5-2

%description -n %{libcos4}
This package contains the library needed to run programs dynamically
linked with omnirb.

%files -n %{libcos4}
%{_libdir}/libCOS%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libcosdynamic4}
Summary:	A robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Conflicts:	%{_lib}omniorb4 < 4.1.5-2

%description -n %{libcosdynamic4}
This package contains the library needed to run programs dynamically
linked with omnirb.

%files -n %{libcosdynamic4}
%{_libdir}/libCOSDynamic%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libcodesets4}
Summary:	A robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Conflicts:	%{_lib}omniorb4 < 4.1.5-2

%description -n %{libcodesets4}
This package contains the library needed to run programs dynamically
linked with omnirb.

%files -n %{libcodesets4}
%{_libdir}/libomniCodeSets%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libconmgmt4}
Summary:	A robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Conflicts:	%{_lib}omniorb4 < 4.1.5-2

%description -n %{libconmgmt4}
This package contains the library needed to run programs dynamically
linked with omnirb.

%files -n %{libconmgmt4}
%{_libdir}/libomniConnectionMgmt%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libdynamic4}
Summary:	A robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Conflicts:	%{_lib}omniorb4 < 4.1.5-2

%description -n %{libdynamic4}
This package contains the library needed to run programs dynamically
linked with omnirb.

%files -n %{libdynamic4}
%{_libdir}/libomniDynamic%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{liborb4}
Summary:	A robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Conflicts:	%{_lib}omniorb4 < 4.1.5-2
Obsoletes:	%{_lib}omniorb4 < 4.1.5-2

%description -n %{liborb4}
This package contains the library needed to run programs dynamically
linked with omnirb.

%files -n %{liborb4}
%{_libdir}/libomniORB%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libssl4}
Summary:	A robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Conflicts:	%{_lib}omniorb4 < 4.1.5-2

%description -n %{libssl4}
This package contains the library needed to run programs dynamically
linked with omnirb.

%files -n %{libssl4}
%{_libdir}/libomnisslTP%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libomnithread}
Summary:	A robust high performance CORBA ORB for C++ and Python
Group:		System/Libraries
Conflicts:	%{_lib}omniorb4 < 4.1.5-2

%description -n %{libomnithread}
This package contains the library needed to run programs dynamically
linked with omnirb.

%files -n %{libomnithread}
%{_libdir}/libomnithread.so.%{thread_major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files and libraries needed for %{name} development
Group:		Development/C++
Requires:	%{libcos4} = %{EVRD}
Requires:	%{libcosdynamic4} = %{EVRD}
Requires:	%{libcodesets4} = %{EVRD}
Requires:	%{libconmgmt4} = %{EVRD}
Requires:	%{libdynamic4} = %{EVRD}
Requires:	%{liborb4} = %{EVRD}
Requires:	%{libssl4} = %{EVRD}
Requires:	%{libomnithread} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package includes the header files and libraries needed for
developing programs using %{name}.

%files -n %{devname}
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
%{_libdir}/pkgconfig/*

#----------------------------------------------------------------------------

%package -n %{name}-doc
Summary:	Documentation for omniORB
Group:		Development/C++

%description -n %{name}-doc
This package includes developers doc including examples.

%files -n %{name}-doc
%doc doc/*

#----------------------------------------------------------------------------

%package -n python-omniidl
Group:		Development/Python
Summary:	OmniOrb IDL compiler

%description -n python-omniidl
OmniOrb IDL compiler.

%files -n python-omniidl
%defattr(-,root,root,755)
%{_bindir}/omniidl*
%{_datadir}/idl/omniORB/*.idl
%{_datadir}/idl/omniORB/COS/*.idl
%dir %{py_puresitedir}/omniidl
%{py_puresitedir}/omniidl/*
%dir %{py_puresitedir}/omniidl_be
%{py_puresitedir}/omniidl_be/*.py*
%dir %{py_puresitedir}/omniidl_be/cxx
%{py_puresitedir}/omniidl_be/cxx/*.py
%{py_puresitedir}/omniidl_be/cxx/*.pyc
%{py_puresitedir}/omniidl_be/cxx/header
%{py_puresitedir}/omniidl_be/cxx/skel
%{py_puresitedir}/omniidl_be/cxx/dynskel
%{py_puresitedir}/omniidl_be/cxx/impl
%{py_platsitedir}/_omniidlmodule.so
%{_libdir}/python%{py_ver}/site-packages/_omniidlmodule.so.*

#----------------------------------------------------------------------------

%prep
%setup -q -n omniORB-%{version}
%patch0 -p1
%patch2 -p0

%build
%configure2_5x --with-openssl=%{_prefix}
%make

%install
%makeinstall_std

install -m 755 -d %{buildroot}%{_mandir}/{man1,man5}
install -m 755 -d %{buildroot}%{_sysconfdir}/init.d
install -m 755 -d %{buildroot}/var/omninames/

install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}
install -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/init.d/omninames

install -m 644 man/man1/* %{buildroot}%{_mandir}/man1/

mkdir -p  %{buildroot}/var/log/omninames
chmod 755 %{buildroot}%{_includedir}/{omnithread,COS,omniORB4,omniORB4/internal}

mkdir -p %{buildroot}%{py_platsitedir}/%{name}
pushd %{buildroot}%{py_platsitedir}/%{name}
python -O -c "import compileall; compileall.compile_dir('.')"
python -c "import compileall; compileall.compile_dir('.')"

