Name:		perftest
Summary:	IB Performance tests
Version:	1.2.3
Release:	3%{?dist}
License:	GPLv2 or BSD
Group:		Productivity/Networking/Diagnostic
Source:		http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}-0.8.g196d994.tar.gz
Url:		http://www.openfabrics.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libibverbs-devel >= 1.1.3, librdmacm-devel >= 1.0.10
Obsoletes:	openib-perftest <= 1.2
ExclusiveArch:	i386 x86_64 ia64 ppc ppc64

%description
gen2 uverbs microbenchmarks

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
make
chmod -x runme

%install
rm -rf %{buildroot}
install -D -m 0755 rdma_lat $RPM_BUILD_ROOT%{_bindir}/rdma_lat
install -D -m 0755 rdma_bw $RPM_BUILD_ROOT%{_bindir}/rdma_bw
install -D -m 0755 ib_write_lat $RPM_BUILD_ROOT%{_bindir}/ib_write_lat
install -D -m 0755 ib_write_bw $RPM_BUILD_ROOT%{_bindir}/ib_write_bw
install -D -m 0755 ib_send_lat $RPM_BUILD_ROOT%{_bindir}/ib_send_lat
install -D -m 0755 ib_send_bw $RPM_BUILD_ROOT%{_bindir}/ib_send_bw
install -D -m 0755 ib_read_lat $RPM_BUILD_ROOT%{_bindir}/ib_read_lat
install -D -m 0755 ib_read_bw $RPM_BUILD_ROOT%{_bindir}/ib_read_bw
install -D -m 0755 ib_write_bw_postlist $RPM_BUILD_ROOT%{_bindir}/ib_write_bw_postlist
install -D -m 0755 ib_clock_test $RPM_BUILD_ROOT%{_bindir}/ib_clock_test

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING runme
%_bindir/*

%changelog
* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 1.2.3-3.el6
- More minor pkgwrangler cleanups
- Related: bz543948

* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 1.2.3-2.el6
- Fixes for pkgwrangler review
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 1.2.3-1.el5
- Update to latest upstream version
- Related: bz518218

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 1.2-14.el5
- Rebuild against libibverbs that isn't missing the proper ppc wmb() macro
- Related: bz506258

* Sun Jun 21 2009 Doug Ledford <dledford@redhat.com> - 1.2-13.el5
- Update to ofed 1.4.1 final bits
- Rebuild against non-XRC libibverbs
- Related: bz506097, bz506258

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 1.2-12.el5
- Update to ofed 1.4.1-rc3 version
- Remove dead patch
- Related: bz459652

* Wed Sep 17 2008 Doug Ledford <dledford@redhat.com> - 1.2-11
- Upstream has updated the tarball without updating the version, so we
  grabbed the one from the OFED-1.3.2-20080728.0355 tarball
- Resolves: bz451481

* Wed Apr 09 2008 Doug Ledford <dledford@redhat.com> - 1.2-10
- Fix the fact that the itc clock on ia64 may be a multiple of the cpu clock
- Resolves: bz433659

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 1.2-9
- Update to OFED 1.3 final bits
- Related: bz428197

* Sun Jan 27 2008 Doug Ledford <dledford@redhat.com> - 1.2-8
- Split out to separate package (used to be part of openib package)
- Related: bz428197

