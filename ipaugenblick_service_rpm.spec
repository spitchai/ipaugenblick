Summary: IPAugenblick service
Name: ipaugenblick_srv
Version: 1.0
Release: 1
License: GPL
Group: Applications/Networking
AutoReq: 0
Packager: Vadim Suraev <vadim.suraev@gmail.com>

%description
User-space full IP stack integrated with DPDK
%prep
OS_VERSION=$(cat /proc/version)
if [[ $OS_VERSION == *"fedora"* ]] || [[ $OS_VERSION == *"Fedora"* ]]
then
	OS_VERSION="Fedora"
elif [[ $OS_VERSION == *"Ubuntu"* ]] || [[ $OS_VERSION == *"ubuntu"* ]]
then
	OS_VERSION="Ubuntu";
fi
rm -rf $RPM_BUILD_ROOT/ipaugenblick
rm -rf $RPM_BUILD_DIR/ipaugenblick
git clone https://github.com/vadimsu/ipaugenblick
cd ipaugenblick
git checkout dpdk-2.0
cd dpdk-2.0.0
make install T=x86_64-native-linuxapp-gcc
cd ..
%build
cd ipaugenblick
./build_version.sh
make CURRENT_DIR=$(pwd)/ RTE_SDK=$(pwd)/dpdk-2.0.0
%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/ipaugenblick
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/include
mkdir -p $RPM_BUILD_ROOT/etc/ipaugenblick
mkdir -p $RPM_BUILD_ROOT/opt/ipaugenblick
if [[ $OS_VERSION == "Fedora" ]]
then
	mkdir -p $RPM_BUILD_ROOT/lib/systemd/system
	mkdir -p $RPM_BUILD_ROOT/etc/systemd/system/
elif [[ $OS_VERSION == "Ubuntu" ]]
	mkdir -p $RPM_BUILD_ROOT/etc/init.d
then
fi
cd $RPM_BUILD_DIR
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_eal.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_timer.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_ring.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_mbuf.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_mempool.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_malloc.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_pmd_ixgbe.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/libethdev.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_cfgfile.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_cmdline.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_hash.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_kvargs.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_meter.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/dpdk-2.0.0/x86_64-native-linuxapp-gcc/lib/librte_pmd_bond.so* $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/stack_and_service/x86_64-native-linuxapp-gcc/libnetinet.so $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/stack_and_service/service/x86_64-native-linuxapp-gcc/ipaugenblick_srv $RPM_BUILD_ROOT/usr/bin/ipaugenblick_srv
cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/ipaugenblick_app_api/stack_and_service/service/ipaugenblick_app_api/x86_64-native-linuxapp-gcc/libipaugenblickservice.so $RPM_BUILD_ROOT/usr/lib/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/ipaugenblick_app_api/ipaugenblick_api.h $RPM_BUILD_ROOT/usr/include/.
cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/dpdk_ip_stack_config.txt $RPM_BUILD_ROOT/etc/ipaugenblick/.
if [[ $OS_VERSION == "Fedora" ]]
then
	cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/ipaugenblick.service.fedora $RPM_BUILD_ROOT/lib/systemd/system/ipaugenblick.service
	cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/ipaugenblick_service.sh $RPM_BUILD_ROOT/usr/bin/ipaugenblick_service.sh
elif [[ $OS_VERSION == "Ubuntu" ]]
	cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/ipaugenblick_service.sh $RPM_BUILD_ROOT/etc/init.d/ipaugenblick_service.sh
then
fi
cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/test_client/*.sh $RPM_BUILD_ROOT/opt/ipaugenblick/.
cp $RPM_BUILD_DIR/ipaugenblick/stack_and_service/service/test_client/*.c $RPM_BUILD_ROOT/opt/ipaugenblick/.
%files
%defattr(-,root,root,-)
/usr/lib/ipaugenblick/librte_eal.so*
/usr/lib/ipaugenblick/librte_timer.so*
/usr/lib/ipaugenblick/librte_ring.so*
/usr/lib/ipaugenblick/librte_mbuf.so*
/usr/lib/ipaugenblick/librte_mempool.so*
/usr/lib/ipaugenblick/librte_malloc.so*
/usr/lib/ipaugenblick/librte_pmd_ixgbe.so*
/usr/lib/ipaugenblick/libethdev.so*
/usr/lib/ipaugenblick/libnetinet.so
/usr/lib/ipaugenblick/libipaugenblickservice.so
/usr/lib/ipaugenblick/librte_cfgfile.so*
/usr/lib/ipaugenblick/librte_cmdline.so*
/usr/lib/ipaugenblick/librte_hash.so*
/usr/lib/ipaugenblick/librte_kvargs.so*
/usr/lib/ipaugenblick/librte_meter.so*
/usr/lib/ipaugenblick/librte_pmd_bond.so*
/usr/bin/ipaugenblick_srv
if [[ $OS_VERSION == "Fedora" ]]
then
	/lib/systemd/system/ipaugenblick.service
	/usr/bin/ipaugenblick_service.sh
elif [[ $OS_VERSION == "Ubuntu" ]]
then
	/etc/init.d/ipaugenblick_service.sh
fi
/usr/include/ipaugenblick_api.h
/opt/ipaugenblick/*
%config
/etc/ipaugenblick/dpdk_ip_stack_config.txt
%post
OS_VERSION=$(cat /proc/version)
if [[ $OS_VERSION == *"fedora"* ]] || [[ $OS_VERSION == *"Fedora"* ]]
then
	cd /etc/systemd/system/
	ln -s /lib/systemd/system/ipaugenblick.service ipaugenblick.service
	systemctl daemon-reload
	systemctl start ipaugenblick.service
	systemctl enable ipaugenblick.service
elif [[ $OS_VERSION == *"Ubuntu"* ]] || [[ $OS_VERSION == *"ubuntu"* ]]
then
	update-rc.d ipaugenblick_service.sh start
	update-rc.d ipaugenblick_service.sh enable
fi
