# TODO: 
# - find homepage 
# - update to 1.5 (i can't find source, only binaries!)
Summary:	A powerful scientific DAL calculator
Summary(pl):	Zaawansowany kalkulator naukowy
Name:		dalc
Version:	0.1
Release:	6
License:	GPL
Group:		Applications/Math
Source0:	http://linuxberg.iol.it/files/console/scientific/%{name}-%{version}.tgz
# Source0-md5:	7720fdddbab2b72932fa58b139bc5be5
Source1:	%{name}.desktop
Patch0:		%{name}-ac_am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-ext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
%endif

%description
Dalc is designed to be both powerful and easy to use at the same time.

%description -l pl
Dalc ma du¿e mo¿liwo¶ci, jednocze¶nie bêd±c ³atwym w u¿yciu.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{makeinstall}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
