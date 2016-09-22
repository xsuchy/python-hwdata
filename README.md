# python-hwdata

Provides python interface to database stored in [hwdata](https://fedorahosted.org/hwdata/) package.
It allows you to get human readable description of USB and PCI devices.


## Example

```
#!/usr/bin/python

from hwdata import PCI, USB, PNP

# for obtaining real id of your devices you can use package python-gudev

pci_vendor_id = '0e11'
pci_device_id = 'b01e'

usb_vendor_id = '03f0'
usb_device_id = '1f12'


pci = PCI()
print("Vendor: %s" % pci.get_vendor(pci_vendor_id))
print("Device: %s" % pci.get_device(pci_vendor_id, pci_device_id))


usb = USB()
print("Vendor: %s" % usb.get_vendor(usb_vendor_id))
print("Device: %s" % usb.get_device(usb_vendor_id, usb_device_id))

pnp = PNP()
print("Vendor: %s" $ pnp.get_vendor('AAA'))
```

## Upstream

https://github.com/xsuchy/python-hwdata

## Build package

When you run:
```
tito build --tgz
```
you will get latest tar.gz file.

When you run:
```
tito build --rpm
```
you will get latest rpm package.

## Distributions

This package is present in [Fedora and EPEL](http://koji.fedoraproject.org/koji/packageinfo?packageID=10271). You should be able to just `yum install python-hwdata`.
