Summary: A fast, versatile, remote (and local) file-copying tool
Name: rsync
Version: 3.0.1
%define fullversion %{version}pre1
Release: 0.1.pre1
Group: Applications/Internet
Source0: http://rsync.samba.org/ftp/rsync/%{name}-%{fullversion}.tar.gz
Source1: http://rsync.samba.org/ftp/rsync/%{name}-patches-%{fullversion}.tar.gz
URL: http://rsync.samba.org/

Prefix: %{_prefix}
BuildRoot: /var/tmp/%{name}-root
License: GPL

%description
Rsync is a fast and extraordinarily versatile file copying tool.  It can
copy locally, to/from another host over any remote shell, or to/from a
remote rsync daemon.  It offers a large number of options that control
every aspect of its behavior and permit very flexible specification of the
set of files to be copied.  It is famous for its delta-transfer algorithm,
which reduces the amount of data sent over the network by sending only the
differences between the source files and the existing files in the
destination.  Rsync is widely used for backups and mirroring and as an
improved copy command for everyday use.

%prep
# Choose one -- setup source only, or setup source + rsync-patches:
%setup -q -n %{name}-%{fullversion}
#%setup -q -n %{name}-%{fullversion} -b1

# If you you used "%setup -q -b1", choose the patches you wish to apply:
#patch -p1 <patches/acls.diff
#patch -p1 <patches/xattrs.diff
#patch -p1 <patches/checksum-reading.diff

%build
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

mkdir -p $RPM_BUILD_ROOT/etc/xinetd.d
install -m 644 packaging/lsb/rsync.xinetd $RPM_BUILD_ROOT/etc/xinetd.d/rsync

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README tech_report.tex
%config(noreplace) /etc/xinetd.d/rsync
%{_prefix}/bin/rsync
%{_mandir}/man1/rsync.1*
%{_mandir}/man5/rsyncd.conf.5*

%changelog
* Mon Mar 24 2008 Wayne Davison <wayned@samba.org>
Released 3.0.1pre1.

* Fri Mar 21 2008 Wayne Davison <wayned@samba.org>
Added installation of /etc/xinetd.d/rsync file and some commented-out
lines that demonstrate how to use the rsync-patches tar file.
