%define	name	lout
%define	version	3.31
%define	release	%mkrel 3

Summary:	The Lout document formatting language
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Text tools
Source0:	ftp://ftp.cs.usyd.edu.au/jeff/lout/%{name}-%{version}.tar.bz2
Patch0:		lout-makefile.patch
License:	GPL
Url:		http://lout.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Lout is a high-level language for document formatting.  Lout reads a
high-level description of a document (similar in style to LaTeX) and can
produce a PostScript(TM) file for printing or produce plain text.
Lout supports the typesetting of documents which contain floating
figures, table, diagrams, rotated and scaled text or graphics, footnotes,
running headers, footers, an index, a table of contents and bibliography,
cross-references, mathematical equations and statistical graphs.  Lout can
be extended with definitions that should be easier to write than other
languages, since Lout is a high-level language.  Lout supports (with
hyphenation) a variety of languages:  Czech, Danish, Dutch, English,
Finnish, French, German, Norwegian, Russian, Slovenian, Spanish and
Swedish.

Install the lout package if you'd like to try the Lout document formatting
system.  Unless you're already a Lout expert, you'll probably want to also
install the lout-doc package, which contains the documentation for Lout.

%package doc
Summary:	The documentation for the Lout document formatting language
Group:		Books/Computer books

%description doc
The lout-doc package includes all of the documentation for the Lout
document formatting language.  The documentation includes manuals for
regular users and for experts, written in Lout and available as
PostScript(TM) files.  The documentation provides good examples for how to
write large documents with Lout.

If you're installing the lout package, you should install the lout-doc
package.

%prep
%setup -q 
%patch0 -p1

%build
%make LIBDIR=%{_datadir}/lout lout prg2lout

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/{bin,doc,man/man1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/

%makeinstall_std DATADIR=%{_datadir} LIBDIR=%{_datadir}/lout installman installdoc

for i in user slides expert design; do
    chmod 755 $RPM_BUILD_ROOT/usr/doc/lout/$i
done

#moves the man page
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_datadir}

# remove unwanted files
rm -rf $RPM_BUILD_ROOT/%_prefix/doc
rm -rf $RPM_BUILD_DIR/%name-%version/doc/user/.pie_intr.swp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,755)
%doc blurb README maillist whatsnew notes_dsc
%defattr(-,root,root)
%{_bindir}/lout
%{_mandir}/man1/*
%{_bindir}/prg2lout
%{_datadir}/lout

%files doc
%defattr(0644,root,root,755)
%doc doc/

