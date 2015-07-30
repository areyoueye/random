import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))
    for services in bluetooth.find_service(address = addr): 
        print "\t Name:           %s" % (services["name"]) 
        print "\t Description:    %s" % (services["description"]) 
        print "\t Protocol:       %s" % (services["protocol"]) 
        print "\t Provider:       %s" % (services["provider"]) 
        print "\t Port:           %s" % (services["port"]) 
        print "\t service-classes %s" % (services["service-classes"])
        print "\t profiles        %s" % (services["profiles"])
        print "\t Service id:  %s" % (services["service-id"]) 
        print "" 

    print '===================================='

