Summary:	A powerful scientific DAL calculator
Summary(pl):	Zaawansowany kalkulator naukowy
Name:		dalc
Version:	0.1
Release:	3
License:	GPL
Group:		Applications/Math
Source0:	http://linuxberg.iol.it/files/console/scientific/%{name}-%{version}.tgz
Patch0:		%{name}-ac_am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		__cxx		%{__cc}

%description
Dalc is designed to be both powerful and easy to use at the same time.

%description -l pl
Dalc ma du¿e mo¿liwo¶ci, jednocze¶nie bêd±c ³atwym w u¿yciu.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
autoheader
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
