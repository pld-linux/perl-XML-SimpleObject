%include	/usr/lib/rpm/macros.perl
Summary:	XML-SimpleObject perl module
Summary(pl):	Modu³ perla XML-SimpleObject
Name:		perl-XML-SimpleObject
Version:	0.41
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-SimpleObject%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SimpleObject is a small and simple package that takes the output
of XML::Parser as a tree, and gives simple methods for accessing the
structure of an XML document. It is very lightweight, but provides the
simplest access to an XML document possible. It does not subclass
XML::Parser; rather, it is meant to serve purely as an object struct
for an outgoing tree.

%description -l pl
XML::SimpleObject jest ma³ym i prostym pakietem pozwalaj±cym na ³atwy
dostêp do struktury dokumentu XML.

%prep
%setup -q -n XML-SimpleObject%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc %{_mandir}/man3/*
%{perl_sitelib}/XML/SimpleObject.pm
