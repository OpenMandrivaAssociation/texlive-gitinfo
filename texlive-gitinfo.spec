Name:		texlive-gitinfo
Version:	34049
Release:	2
Summary:	Access metadata from the git distributed version control system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gitinfo
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitinfo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitinfo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes it possible to incorporate git version
control metadata into documents. Note this version is now
deprecated, but is kept on the archive, pro tem, for continuity
for existing users. For memoir users, the package provides the
means to tailor page headers and footers to use the metadata.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gitinfo/gitinfo.sty
%{_texmfdistdir}/tex/latex/gitinfo/gitsetinfo.sty
%doc %{_texmfdistdir}/doc/latex/gitinfo/README
%doc %{_texmfdistdir}/doc/latex/gitinfo/gitHeadInfo.gin
%doc %{_texmfdistdir}/doc/latex/gitinfo/gitinfo.pdf
%doc %{_texmfdistdir}/doc/latex/gitinfo/gitinfo.tex
%doc %{_texmfdistdir}/doc/latex/gitinfo/post-xxx-sample.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
