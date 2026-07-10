%global tl_name bxcoloremoji
%global tl_revision 79465

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Use color emojis more conveniently
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxcoloremoji
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcoloremoji.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcoloremoji.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(twemojis)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package lets users output color emojis in LaTeX documents. Compared
to other packages with similar functionality, this package has the
following merits: It supports all major LaTeX engines. Emojis can be
entered as the characters themselves, as their Unicode code values, or
as their short names. It works reasonably well in PDF strings when using
hyperref. Emojis can be handled properly even in Japanese typesetting
environments. This package has been widely used among the Japanese LaTeX
community, but there are already many emoji packages on CTAN and in TeX
Live. To avoid uploading a large amount of emoji image data that are
essentially identical, the package was revised in version 1.0 so that
the image output was delegated to the twmojis package. Therefore, this
package now contains no image data.

