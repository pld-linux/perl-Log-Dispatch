%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Dispatch
Summary:	Log::Dispatch -- Dispatches messages to multiple Log::Dispatch::* objects
#Summary(pl):	
Name:		perl-%{pdir}-%{pnam}
Version:	2.01
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Dispatch is a suite of OO modules for logging messages to multiple
outputs, each of which can have a minimum and maximum log level.  It is
designed to be easily subclassed, both for creating a new dispatcher
object and particularly for creating new outputs.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL < /dev/null
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
