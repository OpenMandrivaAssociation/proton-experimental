# FIXME
# gcc -o wine64-preloader -static -nostartfiles -nodefaultlibs -Wl,-Ttext=0x7c400000 preloader.o ../libs/port/libwine_port.a -Oz -gdwarf-4 -Wstrict-aliasing=2 -pipe -Wformat -Werror=format-security  -fstack-protector --param=ssp-buffer-size=4  -fPIC -flto -Wl,-O2  -Wl,--no-undefined -flto
# /tmp/ccHA1ZYg.ltrans0.ltrans.o(.text+0x12): error: undefined reference to 'thread_data'
# /tmp/ccHA1ZYg.ltrans0.ltrans.o(.text+0x2a): error: undefined reference to 'wld_start'
%define _disable_lto 1
# OpenCL support doesn't see cl* functions even with -lCL, but works if built...
%define _disable_ld_no_undefined 1
# Build time errors with lld 9.0.0-rc1 on x86_32 only
# ld: error: can't create dynamic relocation R_386_32 against symbol: .L.str in readonly segment; recompile object files with -fPIC or pass '-Wl,-z,notext' to allow text relocations in the output
%ifarch %{ix86}
%global optflags %{optflags} -Wl,-z,notext -fuse-ld=lld
%global ldflags %{ldflags} -Wl,-z,notext -fuse-ld=lld
%endif

%define _fortify_cflags %{nil}
%define _ssp_cflags %{nil}

%define major 1
%define devname %{mklibname -d wine}

%bcond_with rebuild_unicode

Name:		proton-experimental
Version:	11.0+20260808
%define major %(echo %{version}|cut -d+ -f1)
Release:	1
Source0:	https://github.com/ValveSoftware/wine/archive/refs/heads/experimental_%{major}.tar.gz
Summary:	Proton Experimental - runs MS Windows programs
License:	LGPLv2+
Group:		Emulators
URL:		https://www.winehq.com/

Source2:	wine.binfmt

%define vk_version 1.4.357
Source10:	https://raw.githubusercontent.com/KhronosGroup/Vulkan-Docs/v%{vk_version}/xml/vk.xml
Source11:	https://raw.githubusercontent.com/KhronosGroup/Vulkan-Docs/v%{vk_version}/xml/video.xml

%ifarch %{x86_64}
# Wine needs GCC on x86_64 for MS ABI support. Require the actual
# binaries — a virtual "gcc" provide can be satisfied without /usr/bin/gcc.
BuildRequires:	/usr/bin/gcc
BuildRequires:	/usr/bin/g++
BuildRequires:	binutils
%endif

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gpm-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	pkgconfig(OpenCL)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(sane-backends)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slibtool
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd-sgml
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd-sgml
BuildRequires:	sgml-tools
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(freeglut)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(capi20)
BuildRequires:	pkgconfig(netapi)
BuildRequires:	pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	glibc-static-devel
BuildRequires:	chrpath
BuildRequires:	giflib-devel
BuildRequires:	pkgconfig(xkbregistry)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	icoutils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(ldap)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	valgrind
BuildRequires:	gsm-devel
BuildRequires:	unixODBC-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	gettext-devel
BuildRequires:	%mklibname -d piper2024
BuildRequires:	%mklibname -d vosk
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(osmesa)
BuildRequires:	pkgconfig(libglvnd)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	ieee1284-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	jxrlib-devel
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama) 
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(libvkd3d)
BuildRequires:	pkgconfig(krb5)
BuildRequires:	pkgconfig(com_err)
BuildRequires:	fontforge
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-base-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	cmake(FAudio)

%if %{with rebuild_unicode}
BuildRequires:	perl(XML::LibXML)
%endif
Suggests:	sane-frontends
# wine dlopen's these, so let's add the dependencies ourself
Requires:	%{dlopen_req freetype}
Requires:	%{dlopen_req gnutls}
Requires:	%{dlopen_req asound}
Requires:	%{dlopen_req png}
Requires:	%{dlopen_req OSMesa}
Requires:	%{dlopen_req Xcomposite}
Requires:	%{dlopen_req Xcursor}
Requires:	%{dlopen_req Xinerama}
Requires:	%{dlopen_req Xrandr}
Requires:	%{dlopen_req Xrender}
Requires:	%{dlopen_req v4l2}
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils
Requires(post):	desktop-common-data
Requires(postun):	desktop-common-data
#for winetricks
Requires:	cabextract
Requires:	unzip
Suggests:	webcore-fonts
%rename		winetricks
%ifarch %{x86_64}
# Make sure we have 32-bit versions of DRI drivers... Needed
# as soon as a 32-bit Windows app uses OpenGL or DirectX
Requires:	libdri-drivers
%endif
# (Anssi) If wine-gecko is not installed, wine pops up a dialog on first
# start proposing to download wine-gecko from sourceforge, while recommending
# to use distribution packages instead. Therefore suggest wine-gecko here:
Suggests:	wine-gecko
Suggests:	%{dlopen_req ncursesw}
%ifarch %{ix86} %{x86_64}
BuildRequires:	mingw
BuildRequires:	cross-i686-w64-mingw32-binutils >= 2.38-2
BuildRequires:	cross-i686-w64-mingw32-gcc-bootstrap
BuildRequires:	cross-i686-w64-mingw32-libc
%ifarch %{x86_64}
BuildRequires:	cross-x86_64-w64-mingw32-binutils >= 2.38-2
BuildRequires:	cross-x86_64-w64-mingw32-gcc-bootstrap
BuildRequires:	cross-x86_64-w64-mingw32-libc
%endif
%endif
Recommends:	direct3d-implementation
Recommends:	direct3d12-implementation

%patchlist
proton-vulkan-libm-linkage.patch
proton-9.0-compile.patch
proton-10.0-ffmpeg-8.0.patch
proton-11.0-clang-asm-jmp.patch
proton-11.0-arm-exception-dir-size.patch
proton-11.0-makedep-compiler-rt.patch
proton-11.0-compiler-rt-chkstk.patch
proton-11.0-mscorwks-register.patch
proton-11.0-sqlite3-arm-barrier.patch

%description
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix. It
consists of a program loader which loads and executes a Microsoft
Windows binary, and a library (called Winelib) that implements Windows
API calls using their Unix or X11 equivalents.  The library may also
be used for porting Win32 code into native Unix executables.

%package devel
Summary:	Static libraries and headers for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}
%rename		%{devname}
%rename wine64-devel

%description devel
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix.

%{name}-devel contains the libraries and header files needed to
develop programs which make use of wine.

Wine is often updated.

%package direct3d
Summary:	The Direct3D implementation from the Proton Experimental project
Group:		Emulators
Provides:	direct3d-implementation
Conflicts:	dxvk
Conflicts:	wine-direct3d

%description direct3d
The Direct3D implementation from the Proton Experimental project

Direct3D is a Windows 3D acceleration library used by many games
and applications.

This is one of several alternative implementations of this interface.

wine-direct3d is the original implementation from Wine
proton-direct3d is the implementation from Proton
proton-experimental-direct3d is the implementation from Proton-experimental
dxvk is a reimplementation on top of Vulkan rather than OpenGL

%package direct3d12
Summary:	The Direct3D 12 implementation from the Proton Experimental project
Group:		Emulators
Provides:	direct3d12-implementation
Conflicts:	vkd3d-proton
Conflicts:	wine-direct3d12
Requires:	direct3d-implementation

%description direct3d12
The Direct3D 12 implementation from the Proton Experimental project

Direct3D is a Windows 3D acceleration library used by many games
and applications.

This is one of several alternative implementations of this interface.

wine-direct3d12 is the original implementation from Wine
proton-direct3d12 is the implementation from Proton
proton-experimental-direct3d12 is the implementation from Proton-experimental
vkd3d-proton is a reimplementation on top of Vulkan rather than OpenGL

%prep
%autosetup -p1 -n wine-experimental_%{major}

cd dlls/winevulkan
VK_VERSION=$(grep ^VK_XML_VERSION make_vulkan |cut -d'"' -f2)
if [ "$VK_VERSION" != "%{vk_version}" ]; then
	echo "Update the Vulkan XML files to $VK_VERSION"
	exit 1
fi
export XDG_CACHE_HOME=$(pwd)/xdgcache
mkdir -p xdgcache/wine
cp %{S:10} xdgcache/wine/vk-%{vk_version}.xml
cp %{S:11} xdgcache/wine/video-%{vk_version}.xml
./make_vulkan
cd ../..
tools/make_requests
tools/make_specfiles
%if %{with rebuild_unicode}
tools/make_unicode
%endif

autoreconf -f
aclocal
autoconf

%build
# disable fortify as it breaks wine
# http://bugs.winehq.org/show_bug.cgi?id=24606
# http://bugs.winehq.org/show_bug.cgi?id=25073
%undefine _fortify_cflags
export CFLAGS="$(echo %{optflags} |sed -e 's,-m64,,g;s,-mx32,,g')"
export CXXFLAGS="$(echo %{optflags} |sed -e 's,-m64,,g;s,-mx32,,g')"
export LDFLAGS="$(echo %{build_ldflags} |sed -e 's,-m64,,g;s,-mx32,,g')"
%ifarch %{ix86}
# (Anssi 04/2008) bug #39604
# Some protection systems complain "debugger detected" with our
# -fomit-frame-pointer flag, so disable it.
export CFLAGS="${CFLAGS} -fno-omit-frame-pointer"
%endif

%ifarch %{x86_64}
# As of wine 5.6, clang 10.0:
# winecfg in 64bit mode crashes on startup if built with
# clang. Probably clang doesn't get the M$ ABI right
export CC=gcc
export CXX=g++
%endif

export CONFIGURE_TOP=$(pwd)
mkdir build
cd build
%configure \
	--enable-archs=i386,x86_64,arm,aarch64 \
	--with-mingw=clang \
	--with-pulse \
	--with-gstreamer \
	|| { echo "configure failed. Full config.log:"; cat config.log; exit 1; }

if cat config.log |grep "won't be supported" |grep -q -vE '(OSSv4|capi20)'; then
	echo "Full config.log:"
	cat config.log
	echo "***************************************"
	echo "Missing dependencies detected:"
	echo "(Only missing OSSv4 and capi20 are OK):"
	echo "***************************************"
	cat config.log |grep "won't be supported"
	exit 1
fi

%make_build depend
%make_build

%install
cd build
%make_install LDCONFIG=/bin/true
cd ..

# Danny: dirty:
# install -m755 tools/fnt2bdf -D %{buildroot}%{_bindir}/fnt2bdf

# Allow users to launch Windows programs by just clicking on the .exe file...
install -m755 %{SOURCE2} -D %{buildroot}%{_binfmtdir}/wine.conf

mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
cat > %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged/mandriva-%{name}.menu <<EOF
<!DOCTYPE Menu PUBLIC "-//freedesktop//DTD Menu 1.0//EN"
"http://www.freedesktop.org/standards/menu-spec/menu-1.0.dtd">
<Menu>
    <Name>Applications</Name>
    <Menu>
        <Name>Tools</Name>
        <Menu>
            <Name>Emulators</Name>
            <Menu>
                <Name>Wine</Name>
                <Directory>mandriva-%{name}.directory</Directory>
                <Include>
                    <Category>X-MandrivaLinux-MoreApplications-Emulators-Wine</Category>
                </Include>
            </Menu>
        </Menu>
    </Menu>
</Menu>
EOF

mkdir -p %{buildroot}%{_datadir}/desktop-directories
cat > %{buildroot}%{_datadir}/desktop-directories/mandriva-%{name}.directory <<EOF
[Desktop Entry]
Name=Wine
Icon=%{name}
Type=Directory
EOF

mkdir -p %{buildroot}%{_datadir}/applications/
for i in	winecfg:Configurator \
		notepad:Notepad \
		winefile:File\ Manager \
		regedit:Registry\ Editor \
		winemine:Minesweeper \
		wineboot:Reboot \
		"wineconsole cmd":Command\ Line \
		"wine uninstaller:Wine Software Uninstaller";
do cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-$(echo $i|cut -d: -f1).desktop << EOF
[Desktop Entry]
Name=$(echo $i|cut -d: -f2)
Comment=$(echo $i|cut -d: -f2)
Exec=$(echo $i|cut -d: -f1)
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Emulators-Wine;
EOF
done

# Categories=Emulator does nothing and is added as a workaround to kde #27700
desktop-file-install	--vendor="" \
			--add-mime-type=application/x-zip-compressed \
			--remove-mime-type=application/x-zip-compressed \
			--add-category=Emulator \
			--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/wine.desktop

install -d %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}

# winecfg icon
convert dlls/user32/resources/oic_winlogo.ico[5] %{buildroot}%{_miconsdir}/%{name}.png
convert dlls/user32/resources/oic_winlogo.ico[0] %{buildroot}%{_iconsdir}/%{name}.png
convert dlls/user32/resources/oic_winlogo.ico[1] %{buildroot}%{_liconsdir}/%{name}.png

# notepad icon
convert programs/notepad/notepad.ico[2] %{buildroot}%{_miconsdir}/notepad.png
convert programs/notepad/notepad.ico[7] %{buildroot}%{_iconsdir}/notepad.png
convert programs/notepad/notepad.ico[8] %{buildroot}%{_liconsdir}/notepad.png
# winefile icon
convert programs/winefile/winefile.ico[2] %{buildroot}%{_miconsdir}/winefile.png
convert programs/winefile/winefile.ico[8] %{buildroot}%{_iconsdir}/winefile.png
convert programs/winefile/winefile.ico[7] %{buildroot}%{_liconsdir}/winefile.png
# regedit icon
convert programs/regedit/regedit.ico[2] %{buildroot}%{_miconsdir}/regedit.png
convert programs/regedit/regedit.ico[8] %{buildroot}%{_iconsdir}/regedit.png
convert programs/regedit/regedit.ico[7] %{buildroot}%{_liconsdir}/regedit.png
# winemine icon
convert programs/winemine/winemine.ico[2] %{buildroot}%{_miconsdir}/winemine.png
convert programs/winemine/winemine.ico[8] %{buildroot}%{_iconsdir}/winemine.png
convert programs/winemine/winemine.ico[7] %{buildroot}%{_liconsdir}/winemine.png

# wine uninstaller icon:
convert programs/msiexec/msiexec.ico[2] %{buildroot}%{_miconsdir}/msiexec.png
convert programs/msiexec/msiexec.ico[8] %{buildroot}%{_iconsdir}/msiexec.png
convert programs/msiexec/msiexec.ico[7] %{buildroot}%{_liconsdir}/msiexec.png

# change the icons in the respective .desktop files, in order:
sed -i 's,Icon=%{name},Icon=notepad,' %{buildroot}%{_datadir}/applications/mandriva-%{name}-notepad.desktop
sed -i 's,Icon=%{name},Icon=winefile,' %{buildroot}%{_datadir}/applications/mandriva-%{name}-winefile.desktop
sed -i 's,Icon=%{name},Icon=regedit,' %{buildroot}%{_datadir}/applications/mandriva-%{name}-regedit.desktop
sed -i 's,Icon=%{name},Icon=winemine,' %{buildroot}%{_datadir}/applications/mandriva-%{name}-winemine.desktop
sed -i 's,Icon=%{name},Icon=msiexec,' "%{buildroot}%{_datadir}/applications/mandriva-%{name}-wine uninstaller.desktop"

for i in %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/wine/*/*.so; do
	chrpath -d $i || :
done

%files
%doc ANNOUNCE.md AUTHORS README.md
%{_bindir}/wine
%{_libdir}/wine/*/wine
%{_libdir}/wine/*/wine-preloader
%ifarch %{x86_64}
%{_libdir}/wine/*/wine64
%{_libdir}/wine/*/wine64-preloader
%endif
%config %{_binfmtdir}/wine.conf
%{_bindir}/winecfg
%{_bindir}/wineconsole*
%{_bindir}/wineserver
%{_bindir}/wineboot
%{_bindir}/function_grep.pl
#%{_bindir}/wineprefixcreate
%{_bindir}/msidb
%{_bindir}/msiexec
%{_bindir}/notepad
%{_bindir}/regedit
%{_bindir}/winemine
%{_bindir}/winepath
%{_bindir}/regsvr32
%{_bindir}/winefile
%doc %{_mandir}/man1/wine.1*
%doc %lang(de) %{_mandir}/de.UTF-8/man1/wine.1*
%doc %lang(de) %{_mandir}/de.UTF-8/man1/winemaker.1*
%doc %lang(de) %{_mandir}/de.UTF-8/man1/wineserver.1*
%doc %lang(pl) %{_mandir}/pl.UTF-8/man1/wine.1*
%doc %lang(fr) %{_mandir}/fr.UTF-8/man1/*
%doc %{_mandir}/man1/wineserver.1*
%doc %{_mandir}/man1/msiexec.1*
%doc %{_mandir}/man1/notepad.1*
%doc %{_mandir}/man1/regedit.1*
%doc %{_mandir}/man1/regsvr32.1*
%doc %{_mandir}/man1/wineboot.1*
%doc %{_mandir}/man1/winecfg.1*
%doc %{_mandir}/man1/wineconsole.1*
%doc %{_mandir}/man1/winecpp.1*
%doc %{_mandir}/man1/winefile.1*
%doc %{_mandir}/man1/winemine.1*
%doc %{_mandir}/man1/winepath.1*
%dir %{_datadir}/wine
%{_datadir}/wine/wine.inf
%{_datadir}/wine/nls/l_intl.nls
%{_datadir}/wine/nls/locale.nls
%{_datadir}/wine/nls/c_*
%{_datadir}/wine/nls/normidna.nls
%{_datadir}/wine/nls/normnfc.nls
%{_datadir}/wine/nls/normnfd.nls
%{_datadir}/wine/nls/normnfkc.nls
%{_datadir}/wine/nls/normnfkd.nls
%{_datadir}/wine/nls/sortdefault.nls
%{_datadir}/wine/winmd
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/menus/applications-merged/mandriva-%{name}.menu
%{_datadir}/desktop-directories/mandriva-%{name}.directory
%dir %{_datadir}/wine/fonts
%{_datadir}/wine/fonts/*
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%dir %{_libdir}/wine
%ifarch %{x86_64}
%dir %{_libdir}/wine/x86_64-unix
%{_libdir}/wine/x86_64-unix/*.so
%endif
%ifarch %{aarch64}
%dir %{_libdir}/wine/aarch64-unix
%{_libdir}/wine/aarch64-unix/*.so
%endif
# PE modules for every --enable-archs target (host unix libs are above)
%dir %{_libdir}/wine/x86_64-windows
%{_libdir}/wine/x86_64-windows/*.acm
%{_libdir}/wine/x86_64-windows/*.ax
%{_libdir}/wine/x86_64-windows/*.com
%{_libdir}/wine/x86_64-windows/*.cpl
%{_libdir}/wine/x86_64-windows/*.dll
%{_libdir}/wine/x86_64-windows/*.drv
%{_libdir}/wine/x86_64-windows/*.ds
%{_libdir}/wine/x86_64-windows/*.exe
%{_libdir}/wine/x86_64-windows/*.ocx
%{_libdir}/wine/x86_64-windows/*.sys
%{_libdir}/wine/x86_64-windows/*.tlb
%{_libdir}/wine/x86_64-windows/*.msstyles
%exclude %{_libdir}/wine/x86_64-windows/d3d8.dll
%exclude %{_libdir}/wine/x86_64-windows/d3d9.dll
%exclude %{_libdir}/wine/x86_64-windows/d3d10core.dll
%exclude %{_libdir}/wine/x86_64-windows/d3d11.dll
%exclude %{_libdir}/wine/x86_64-windows/d3d12core.dll
%exclude %{_libdir}/wine/x86_64-windows/d3d12.dll
%exclude %{_libdir}/wine/x86_64-windows/dxgi.dll
%dir %{_libdir}/wine/aarch64-windows
%{_libdir}/wine/aarch64-windows/*.acm
%{_libdir}/wine/aarch64-windows/*.ax
%{_libdir}/wine/aarch64-windows/*.com
%{_libdir}/wine/aarch64-windows/*.cpl
%{_libdir}/wine/aarch64-windows/*.dll
%{_libdir}/wine/aarch64-windows/*.drv
%{_libdir}/wine/aarch64-windows/*.ds
%{_libdir}/wine/aarch64-windows/*.exe
%{_libdir}/wine/aarch64-windows/*.ocx
%{_libdir}/wine/aarch64-windows/*.sys
%{_libdir}/wine/aarch64-windows/*.tlb
%{_libdir}/wine/aarch64-windows/*.msstyles
%exclude %{_libdir}/wine/aarch64-windows/d3d8.dll
%exclude %{_libdir}/wine/aarch64-windows/d3d9.dll
%exclude %{_libdir}/wine/aarch64-windows/d3d10core.dll
%exclude %{_libdir}/wine/aarch64-windows/d3d11.dll
%exclude %{_libdir}/wine/aarch64-windows/d3d12core.dll
%exclude %{_libdir}/wine/aarch64-windows/d3d12.dll
%exclude %{_libdir}/wine/aarch64-windows/dxgi.dll
%dir %{_libdir}/wine/arm-windows
%{_libdir}/wine/arm-*/*.acm
%{_libdir}/wine/arm-*/*.ax
%{_libdir}/wine/arm-*/*.com
%{_libdir}/wine/arm-*/*.cpl
%{_libdir}/wine/arm-*/*.dll
%{_libdir}/wine/arm-*/*.drv
%{_libdir}/wine/arm-*/*.ds
%{_libdir}/wine/arm-*/*.exe
%{_libdir}/wine/arm-*/*.ocx
%{_libdir}/wine/arm-*/*.sys
%{_libdir}/wine/arm-*/*.tlb
%{_libdir}/wine/arm-*/*.msstyles
%exclude %{_libdir}/wine/arm-*/d3d8.dll
%exclude %{_libdir}/wine/arm-*/d3d9.dll
%exclude %{_libdir}/wine/arm-*/d3d10core.dll
%exclude %{_libdir}/wine/arm-*/d3d11.dll
%exclude %{_libdir}/wine/arm-*/d3d12core.dll
%exclude %{_libdir}/wine/arm-*/d3d12.dll
%exclude %{_libdir}/wine/arm-*/dxgi.dll
%dir %{_libdir}/wine/i386-windows
# i386 PE (multiarch; no separate 32-bit unix libs with PE multiarch)
%{_libdir}/wine/i386-*/*.acm
%{_libdir}/wine/i386-*/*.ax
%{_libdir}/wine/i386-*/*.com
%{_libdir}/wine/i386-*/*.cpl
%{_libdir}/wine/i386-*/*.dll
%{_libdir}/wine/i386-*/*.drv
%{_libdir}/wine/i386-*/*.ds
%{_libdir}/wine/i386-*/*.exe
%{_libdir}/wine/i386-*/*.msstyles
%{_libdir}/wine/i386-*/*.ocx
%{_libdir}/wine/i386-*/*.sys
%{_libdir}/wine/i386-*/*.tlb
%{_libdir}/wine/i386-*/*.vxd
%{_libdir}/wine/i386-*/*.dll16
%{_libdir}/wine/i386-*/*.exe16
%{_libdir}/wine/i386-*/*.drv16
%{_libdir}/wine/i386-*/*.mod16
%exclude %{_libdir}/wine/i386-*/d3d8.dll
%exclude %{_libdir}/wine/i386-*/d3d9.dll
%exclude %{_libdir}/wine/i386-*/d3d10core.dll
%exclude %{_libdir}/wine/i386-*/d3d11.dll
%exclude %{_libdir}/wine/i386-*/d3d12core.dll
%exclude %{_libdir}/wine/i386-*/d3d12.dll
%exclude %{_libdir}/wine/i386-*/dxgi.dll

%files direct3d
%{_libdir}/wine/aarch64-*/d3d8.dll
%{_libdir}/wine/aarch64-*/d3d9.dll
%{_libdir}/wine/aarch64-*/d3d10core.dll
%{_libdir}/wine/aarch64-*/d3d11.dll
%{_libdir}/wine/aarch64-*/dxgi.dll
%{_libdir}/wine/arm-*/d3d8.dll
%{_libdir}/wine/arm-*/d3d9.dll
%{_libdir}/wine/arm-*/d3d10core.dll
%{_libdir}/wine/arm-*/d3d11.dll
%{_libdir}/wine/arm-*/dxgi.dll
%{_libdir}/wine/x86_64-*/d3d8.dll
%{_libdir}/wine/x86_64-*/d3d9.dll
%{_libdir}/wine/x86_64-*/d3d10core.dll
%{_libdir}/wine/x86_64-*/d3d11.dll
%{_libdir}/wine/x86_64-*/dxgi.dll
%{_libdir}/wine/i386-*/d3d8.dll
%{_libdir}/wine/i386-*/d3d9.dll
%{_libdir}/wine/i386-*/d3d10core.dll
%{_libdir}/wine/i386-*/d3d11.dll
%{_libdir}/wine/i386-*/dxgi.dll

%files direct3d12
%{_libdir}/wine/*-*/d3d12core.dll
%{_libdir}/wine/*-*/d3d12.dll

%files devel
%{_libdir}/wine/*/*.a
%{_includedir}/*
# %{_bindir}/fnt2bdf
%{_bindir}/wmc
%{_bindir}/wrc
%{_bindir}/winebuild
%{_bindir}/winegcc
%{_bindir}/wineg++
%{_bindir}/winecpp
%{_bindir}/widl
%{_bindir}/winedbg
%{_bindir}/winemaker
%{_bindir}/winedump
%doc %{_mandir}/man1/wmc.1*
%doc %{_mandir}/man1/wrc.1*
%doc %{_mandir}/man1/winebuild.1*
%doc %{_mandir}/man1/winemaker.1*
%doc %{_mandir}/man1/winedump.1*
%doc %{_mandir}/man1/widl.1*
%doc %{_mandir}/man1/winedbg.1*
%doc %{_mandir}/man1/wineg++.1*
%doc %{_mandir}/man1/winegcc.1*
