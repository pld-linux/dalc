Summary:	A powerful scientific DAL calculator
Summary(pl):	Zaawansowany kalkulator naukowy
Name:		dalc
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	http://linuxberg.iol.it/files/console/scientific/%{name}-%{version}.tgz
Patch0:		%{name}-fixincludes.patch
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dalc is designed to be both powerful and easy to use at the same time.

%description -l pl
Dalc ma du¿e mo¿liwo¶ci, jednocze¶nie bêd±c ³atwym w u¿yciu.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} \
	-DVIEWER=\\\"xv\\\" -DCONVERTER=\\\"ppmtogif\\\" -I%{_includedir}/ncurses" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

%{__make} install \
        BINDIR=$RPM_BUILD_ROOT%{_bindir} \
        MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
