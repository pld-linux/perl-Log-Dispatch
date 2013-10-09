#
# Conditional build:
%bcond_without	tests	# do not perform "./Build test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Log
%define		pnam	Dispatch
Summary:	Log::Dispatch Perl module - dispatches messages to multiple Log::Dispatch::* objects
Summary(pl.UTF-8):	Moduł Perla Log::Dispatch - wysyłanie komunikatów do wielu obiektów Log::Dispatch::*
Name:		perl-Log-Dispatch
Version:	2.41
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Log/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	85a384db37c7fe4e5db90c0bbc376da2
URL:		http://search.cpan.org/dist/Log-Dispatch/
BuildRequires:	perl-Module-Build >= 0.20
BuildRequires:	perl-Params-Validate >= 0.15
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq	'perl(Apache::Log)' 'perl(MIME::Lite)' 'perl(Mail::Send)' 'perl(Mail::Sender)' 'perl(Mail::Sendmail)'

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
obiektów wysyłających, jak i (szczególnie) nowych wyjść.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/*.pm
%{perl_vendorlib}/Log/Dispatch
%{_mandir}/man3/*
