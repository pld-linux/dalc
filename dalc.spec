Summary:	A powerful scientific DAL calculator
Summary(pl):	Zaawansowany kalkulator naukowy
Name:		dalc
Version:	0.1
Release:	3
License:	GPL
Group:		Applications/Math
Group(cs):	Aplikace/Matematick�
Group(da):	Programmer/Matematik
Group(de):	Applikationen/Mathematik
Group(es):	Aplicaciones/Matem�ticas
Group(fr):	Applications/Math�matiques
Group(it):	Applicazioni/Matematiche
Group(no):	Applikasjoner/Matematiske
Group(pl):	Aplikacje/Matematyczne
Group(pt):	Aplica��es/Matem�tica
Group(ru):	����������/��������������
Group(sl):	Programi/Matemati�ni
Group(sv):	Till�mpningar/Matemataisk
Group(uk):	�������Φ ��������/����������
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
Dalc ma du�e mo�liwo�ci, jednocze�nie b�d�c �atwym w u�yciu.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
autoheader
automake -a -c
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
