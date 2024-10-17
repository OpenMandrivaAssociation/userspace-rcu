%define major 8
%define oldlibname %mklibname urcu 8
%define libname %mklibname urcu
%define develname %mklibname urcu -d
%define gitdate 20240328

Name:		userspace-rcu
Summary:	Userspace RCU (read-copy-update) library
Version:	0.14.1
Release:	%{?gitdate:0.%{gitdate}.}1
License:	LGPLv2.1+
Group:		System/Libraries
URL:		https://lttng.org/urcu
%if 0%{?gitdate:1}
Source0:	https://git.liburcu.org/?p=userspace-rcu.git;a=snapshot;h=HEAD;sf=tgz#/urcu-%{gitdate}.tar.xz
%else
Source0:	http://lttng.org/files/urcu/%{name}-%{version}.tar.bz2
%endif
#Patch0:		urcu-generic-buildfix-arm-clang.patch
BuildRequires:	slibtool

%description
liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales linearly
with the number of cores. It does so by allowing multiples copies of a given
data structure to live at the same time, and by monitoring the data structure
accesses to detect grace periods after which memory reclamation is possible.

%package -n %{libname}
Summary:	Userspace RCU (read-copy-update) library
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales linearly
with the number of cores. It does so by allowing multiples copies of a given
data structure to live at the same time, and by monitoring the data structure
accesses to detect grace periods after which memory reclamation is possible.

%package -n %{develname}
Summary:	Development files for liburcu
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{develname}
Development file for the userspace RCU library (liburcu).

%prep
%autosetup -p1 -n userspace-rcu-%{?gitdate:HEAD-8c5aef6}%{!?gitdate:%{version}}

[ -e configure ] || ./bootstrap
%configure --disable-static --enable-compiler-atomic-builtins

%build
%make_build LIBTOOL=slibtool-shared

%install
%make_install LIBTOOL=slibtool-shared

%files -n %{libname}
%{_libdir}/liburcu*.so.%{major}*

%files -n %{develname}
%{_includedir}/urcu/
%{_includedir}/urcu*.h
%{_libdir}/liburcu*.so
%{_libdir}/pkgconfig/liburcu*.pc
%doc %{_docdir}/userspace-rcu
