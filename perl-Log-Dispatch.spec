#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Log
%define		pnam	Dispatch
Summary:	Log::Dispatch Perl module - dispatches messages to multiple Log::Dispatch::* objects
Summary(pl.UTF-8):	Moduł Perla Log::Dispatch - wysyłanie komunikatów do wielu obiektów Log::Dispatch::*
Name:		perl-Log-Dispatch
Version:	2.70
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Log/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3369ffd45dc098ef6c74622ceee7ad74
URL:		https://metacpan.org/dist/Log-Dispatch
BuildRequires:	perl-Dist-CheckConflicts >= 0.02
BuildRequires:	perl-Params-Validate >= 1.03
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Devel-GlobalDestruction
BuildRequires:	perl-Sys-Syslog >= 0.28
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Specio >= 0.32
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq_perl	MIME::Lite Mail::Send Mail::Sender Mail::Sendmail

%description
Log::Dispatch is a suite of OO modules for logging messages to
multiple outputs, each of which can have a minimum and maximum log
level. It is designed to be easily subclassed, both for creating a new
dispatcher object and particularly for creating new outputs.

%description -l pl.UTF-8
Log::Dispatch to zestaw obiektowo zorientowanych modułów do logowania
komunikatów na wiele wyjść, z których każde może mieć podany minimalny
i maksymalny poziom logowania. Pakiet ten został zaprojektowany tak,
by łatwo można było stworzyć klasy potomne, w celu tworzenia nowych
obiektów dyspozytorów, jak i (w szczególności) nowych wyjść.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/Log/Dispatch.pm
%{perl_vendorlib}/Log/Dispatch
%{_mandir}/man3/Log::Dispatch*.3pm*
