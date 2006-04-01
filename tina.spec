
# TODO: there's a version for sparc, too - but I'm not sure if it not only works on Solaris

Summary:	tina - TIme petri Net Analyzer
Summary(pl):	tina - TIme petri Net Analyzer
Name:		tina
Version:	2.8.0
Release:	0.beta.1
License:	Freeware
Group:		Applications
Source0:	http://www2.laas.fr/tina/%{name}-%{version}-i386-linux.tar.gz
# Source0-md5:	5e83e713e4d04514a614fb91c990787f
URL:		http://www2.laas.fr/tina/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         no_install_post_strip   1

%description
Tina is a toolbox for the edition and analysis of Petri Nets and Time Petri
Nets, developed in the OLC group of LAAS/CNRS.

%description -l pl
Tina to zestaw narz�dzi do edycji oraz analizy sieci Petriego i Czasowych
Sieci Petriego, rozwijany przez grup� OLC w LAAS/CNRS.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/mann}
cp -rf bin/* $RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{_bindir}/plugins $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -Rf extras nets $RPM_BUILD_ROOT%{_datadir}/%{name}
install doc/man/mann/* $RPM_BUILD_ROOT%{_mandir}/mann

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL CHANGES doc/{formats,txt}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/mann/*
