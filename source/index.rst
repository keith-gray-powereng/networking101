.. Networking 101 documentation master file, created by
   sphinx-quickstart on Thu Jun 27 09:52:12 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Networking 101
==============

How the Internet Works!
-----------------------

Purpose & Learning Objectives
-----------------------------

The purpose of this presentation is to bring everyone in SAS up to speed on the basics of networking

At the end of this presenation you will understand the various layers in the networking models.

Outline
=======

.. contents:: 
   :depth: 1

Introduction
============

About Me
--------

* 9th Year with POWER
* Offices

  + STL
  + Boise
  + Hailey

* Expertise

  + SCADA
  + Protection
  + SCADA

* Main Clients

  + Tesoro
  + SSVEC
  + Navy

History of SCADA
----------------

Serial

Why is networking important?
----------------------------

SCADA
~~~~~

* Moving from Serial connections (RS-232, RS485) to Ethernet

  * Existing protocols: Modbus and DNP

* New protocols don't even support serial

  * IEC-61850 MMS

Protection
~~~~~~~~~~

* Moving from Hardwired and Serial connections to Ethernet

  * IEC 61850 GOOSE

* New protocols rely on the speed of Ethernet to function

  * IEC 61850 GOOSE and SV

Network Design
~~~~~~~~~~~~~~

We are being asked by our clients to design substation, and larger area, networks

Network Layer Modeling
======================

Two Main Layer Models
---------------------

* OSI 7 Layer Model
* TCP/IP Model

OSI 7 Layer Model
-----------------

* Layer 1: Physical Layer
* Layer 2: Data Link Layer
* Layer 3: Network Layer
* Layer 4: Transport Layer
* Layer 5: Session Layer
* Layer 6: Presentation Layer
* Layer 7: Application Layer

Layer 1: Physical Layer
-----------------------
* Data Unit: Bit
* Media 
  
  * Fiber
  * Copper
  * Radio

* Signal and binary transmission

  * What is a 1 and what is a 0?
  * Manchester encoding
  * Light Modulation

Layer 2: Data Link Layer
------------------------
* Data Unit: Frame
* Framing, Physical addressing, Error Control, Media Access Control
* Communication within the same network

Layer 3: Network Layer
----------------------
* Data Unit: Packet/Datagram
* Path determination and logical addressing
* Communication between networks aka Routing

Layer 4: Transport Layer
--------------------------
* Data Unit: Segments
* End-to-end connection, reliability and flow control

Layer 5: Session Layer
----------------------
* Data Unit: Data
* Interhost communication, managing sessions between applications

Layer 6: Presentation Layer
---------------------------
* Data Unit: Data
* Data representation, encryption and decryption, convert machine dependent data to machine independent data

Layer 7: Application Layer
--------------------------
* Data Unit: Data
* Network process to application

TCP/IP Model
------------

* Layer 1: Link Layer
* Layer 2: Internet Layer
* Layer 3: Transport Layer
* Layer 4: Application layer

Layer 1: Link Layer
-----------------------
* Corresponds to OSI Model Layers 1 (Physical) and 2 (Data Link)
* Responsible for sending/receiving data on the local network

Layer 2: Internet Layer
------------------------
* Corresponds to OSI Model Layer 3 (Network)
* Responsible for sending/receiving data across 2 or more networks

Layer 3: Transport Layer
------------------------
* Corresponds to OSI Model Layer 4 (Transport)
* Responsible for sending/receiving data between hosts

Layer 4: Application Layer
--------------------------
* Corresponds to OSI Model Layers 5 (Session), 6 (Presentation), and 7 (Application)
* Responsible for sending/receiving data between applications
* Responsible for formatting and presenting data

How do the models work?
-----------------------

.. image:: network-layers.svg


Which Model?
------------

Both models are in use today so we need to keep both of them in mind during today's presentation. Most of the references to a specific layer will be referring to the OSI 7 Layer Model.

Layer Details
=============

Physical and Data Link Layers - Ethernet
========================================


Physical Layer
--------------

* Covers Physical Layer

* Copper

  + 10BASE-T
  + 100BASE-TX
  + 1000BASE-T

* Fiber

  + 10BASE-FL
  + 100BASE-SX
  + 100BASE-FX
  + 100BASE-BX
  + 100BASE-LX
  + 1000BASE-SX
  + 1000BASE-LX

Data Link Layer
---------------

* Covers Data Link Layer
* MAC Addresses
* VLANs
* Data Encapsulation
* CRC
* Carrier sense multiple access with collision detection

Frame Structure
---------------
* Preamble: 7 octets (bytes)
* Start of Frame Delimiter: 1 octet
* Destination MAC: 6 octets
* Source MAC: 6 octets
* VLAN Tag: 4 octets (optional)
* Ethertype or Length: 2 octets
* Payload: 46 - 1500 octets
* Frame Check Sequence: 4 octets
* Interframe Gap: 12 octets

Total Frame size range: 88 to 1542 (including VLAN tag option)

MAC Address
-----------

Types
-----

* Unicast
* Broadcast
* Multicast

Unicast
-------

* Globally Unique
* 6 octets
* First 3 octets are assigned to the manufacturer by the IANA
* Last 3 octets are assigned by the manufacturer
* My laptop NIC address: 5C-26-0A-4A-DA-4F
* 5C-26-0A is assigned to Dell Inc.
* 4A-DA-4F is assigned by Dell to my NIC

  + Useful during troubleshooting (show laptop wireshark here)

* Hosts only accept unicast messages with its MAC address in the destination field of the frame
* Most substation LAN traffic is unicast

Unicast Message
---------------
.. image:: unicast-message.svg


Broadcast
---------

* All hosts accept broadcast frames
* Switches forward broadcast frames out all ports (except the source port)
* MAC Address of all 1s (FF-FF-FF-FF-FF-FF)
* Broadcast is used on a limited basis in all substation LANs

Broadcast Message
-----------------
.. image:: broadcast-message.svg

Multicast
---------

* Hosts are programmed to accept multicast messages
* Least Significant bit of the most significant destination address octet is 1
* Multicast was not used very often in substation LANs, until now!

  + **GOOSE**

Multicast Message
-----------------
.. image:: broadcast-message.svg

.. class:: fragment
   
        Hey, wait a minute! Isn't that the same thing we saw for broadcast?


        Yes it is. Remember that it is up to the network adapter in the host to 
        filter incoming multicast messages

        + Unless programming is done in the switches to filter the messages

VLAN
----

* Virtual Local Area Network
* Typically used by network administrators to separate network users
* GOOSE is another application - we will see this later
* Creates a number of virtual switches inside of a physical switch
* Alternative to separate hardware (switches, fiber, copper) for each application
* VLAN tag also incorporates a priority code - we will see this later
* Note that Microsoft Windows probably will not allows Wireshark to display VLAN tag information

  + Linux will always make it available

Network Layer - Internet Protocol (IP)
======================================

IP
--

* Layer 3 Protocol
* IPv4 - Best Known
* IPv6 - Starting to hear about it, not officially supported on any substation device I know of

IPv4 Addresses
--------------

* Dotted-decimal notation
* 4 octets separated by dots
* 10.123.7.50

IPv4 Subnetting
---------------

* Classless Inter-Domain Routing (CIDR)
* Subnet Mask

  + Dotted-decimal notation
  + 4 octets separated by dots
  + Starts with all 1s, ends with all 0s

    - 255.255.255.0

  + Also found in CIDR notation as '/<number_of_ones>'

    - 10.123.7.50/24 (This is the same as a subnet mask of 255.255.255.0)

Let's Do Some IP Math!
----------------------

* My laptop IP address is 10.123.7.50/24
* I want to ping 10.123.7.1
* Are the two IPs on the same network?



My IP Address AND Subnet Mask
-----------------------------

   +---------------+--------------+--------------+--------------+--------------+
   | 10.123.7.50   | 00001010     | 01111011     | 00000111     | 00110010     |
   +---------------+--------------+--------------+--------------+--------------+
   | 255.255.255.0 | 11111111     | 11111111     | 11111111     | 00000000     |
   +---------------+--------------+--------------+--------------+--------------+
   | 10.123.7.0    | **00001010** | **01111011** | **00000111** | **00000000** |
   +---------------+--------------+--------------+--------------+--------------+

Destination IP Address AND Subnet Mask
--------------------------------------

   +---------------+--------------+--------------+--------------+--------------+
   | 10.123.7.1    | 00001010     | 01111011     | 00000111     | 00000001     |
   +---------------+--------------+--------------+--------------+--------------+
   | 255.255.255.0 | 11111111     | 11111111     | 11111111     | 00000000     |
   +---------------+--------------+--------------+--------------+--------------+
   | 10.123.7.0    | **00001010** | **01111011** | **00000111** | **00000000** |
   +---------------+--------------+--------------+--------------+--------------+

Compare the Results
-------------------

   +---------------+--------------+--------------+--------------+--------------+
   | 10.123.7.0    | **00001010** | **01111011** | **00000111** | **00000000** |
   +---------------+--------------+--------------+--------------+--------------+
   | 10.123.7.0    | **00001010** | **01111011** | **00000111** | **00000000** |
   +---------------+--------------+--------------+--------------+--------------+

They match! The two computers are on the same network and can communicate directly

.. class:: fragment

   But How Exactly?  Over Ethernet using source and destination MAC addresses.

   But how does my laptop know the MAC address of the destination?

Address Resolution Protocol (ARP)
---------------------------------

* ARP is another layer 3 protocol, just like IP
* ARP resolves IP addresses to MAC Addresses
* Every host using Ethernet and IP has ARP
* View the IP to MAC mapping table

.. class:: prettyprint lang-bash

   arp -a #on windows

.. class:: prettyprint lang-bash

   arp #on linux

.. class:: fragment

        **But the ARP table is Blank**

Populating the ARP Table
------------------------

* Two ways the ARP table gets populated

  #. Receiving IP Packets
     
     * The source MAC and IP addresses are included in the message, just record it in the table

  #. Asking

     * Explicitly sending an ARP request

ARP Request
-----------

* ARP packet is sent asking which MAC address owns the IP address in question
* What MAC Address is it sent to?

.. class:: fragment

   **FF-FF-FF-FF-FF-FF**

ARP Request
-----------

* Who responds

.. class:: fragment
   
   **Only the host with the IP address being asked about**

ARP Response
------------

* How does the Requesting host get the information from the response?

.. class:: fragment

   **Responding host uses a unicast message which contains its MAC and IP addresses**


Transport Layer Protocols - TCP/UDP
===================================

TCP/UDP
-------

* TCP (Transport Control Protocol)

  + Connection Oriented
  + 3-way handshake

* UDP (User Datagram Protocol)

  + Connection-less
  + Fire-and-forget

* Mailbox Analogy

Ports
-----

* IANA assigns standard TCP/UDP ports to protocols

  * 20000: DNP
  * 502: Modbus
  * 22: SSH
  * 23: Telnet
  * 80: HTTP (Web)
  * 443: HTTPS (Secure Web)
  * ...and so on

Transmission Control Protocol
-----------------------------

* Connection Oriented
* 3-way handshake

  * SYN
  * SYN, ACK
  * ACK

* Flow control
* Ordering
* Reliable transmission

  * Acknowledgements

User Datagram Protocol
----------------------

* Connectionless
* No handshake
* Relies on upper layers for reliability
* Relies on upper layers for flow control

Comments
--------

* DNP uses either TCP or UDP

  * Overwhelming majority of cases use TCP

* Modbus uses TCP
* MMS uses TCP
* Ruggedcom has a working implentation of GOOSE over UDP

  * They are working to make it part of the standard
  * This would allow GOOSE between networks

Hardware
========

Common Hardware
---------------

* Hub
* Switch
* Router

Hub
---

* Single data bus inside
* Single Broadcast Domain
* Single Collision Domain

Switch
------
* Switches data based on destination MAC Address
* Single Broadcast Domain
* Per Port Collision Domain

Router
------
* Routes Data based on Destination IP Address
* Per Port Broadcast Domain
* Per Port Collision Domain

Classes of Service
==================

Standard
--------

* PCP field in the TCI field of the VLAN header
* 3-bit field => 8 Priority Levels

  * 0 = best effort
  * 7 = highest priority

Implementations
---------------

* Many vendors support 2 priority buffers
* Ruggedcom supports 4
* Anyone know any other switches?
* Need to map standard priorities to available buffers

Example Mapping
---------------

+----------+--------+-----------------------------------+
| PRIORITY | COS    | DESCRIPTION                       |
+==========+========+===================================+
| 0        | NORMAL | All other traffic                 |
+----------+--------+-----------------------------------+
| 1        | NORMAL | reserved for future               |
+----------+--------+-----------------------------------+
| 2        | NORMAL | reserved for future               |
+----------+--------+-----------------------------------+
| 3        | MEDIUM | reserved for future               |
+----------+--------+-----------------------------------+
| 4        | MEDIUM | GOOSE with analog values          |
+----------+--------+-----------------------------------+
| 5        | HIGH   | reserved for future               |
+----------+--------+-----------------------------------+
| 6        | HIGH   | GOOSE without Tripping Capability |
+----------+--------+-----------------------------------+
| 7        | CRIT   | GOOSE with Tripping Capability    |
+----------+--------+-----------------------------------+

Additional Topics
=================

* GOOSE Multicast
* GOOSE VLAN
* VPN
* Gateway Redundancy (VRRP)

References
==========

Page 1
------
* `wikipedia_osi_model`_
* `wikipedia_internet_model`_
* `wikipedia_ethernet_frame`_
* `wikipedia_ethernet`_
* `wikipedia_ethernet_bit_rates`_
* `wikipedia_fast_ethernet`_
* `wikipedia_gigabit_ethernet`_
* `mac_find`_
* `wikipedia_vlan`_
* `wikipedia_mac`_
* `wikipedia_ip_address`_
* `wikipedia_tcp`_
* `wikipedia_udp`_

Page 2
------
* Data Communications and Networking by Behrouz A. Forouzan
* The All-New Switch Book by Rich Seifert and James Edwards

Questions
=========

Thank you for your time!

This concludes the educational content of this activity.

Keith Gray

Project Engineer II

314-851-4064

`POWER Engineers`_

.. _wikipedia_osi_model: http://en.wikipedia.org/wiki/OSI_model
.. _wikipedia_internet_model: http://en.wikipedia.org/wiki/Internet_protocol_suite
.. _wikipedia_ethernet_frame: http://en.wikipedia.org/wiki/Ethernet_frame
.. _wikipedia_ethernet: http://en.wikipedia.org/wiki/Ethernet
.. _wikipedia_ethernet_bit_rates: http://en.wikipedia.org/wiki/List_of_device_bit_rates
.. _wikipedia_fast_ethernet: http://en.wikipedia.org/wiki/Fast_Ethernet
.. _wikipedia_gigabit_ethernet: http://en.wikipedia.org/wiki/Gigabit_Ethernet
.. _mac_find: http://www.coffer.com/mac_find/
.. _wikipedia_vlan: http://en.wikipedia.org/wiki/802.1Q
.. _wikipedia_mac: http://en.wikipedia.org/wiki/MAC_address
.. _wikipedia_ip_address: http://en.wikipedia.org/wiki/IP_address
.. _`POWER Engineers`: http://www.powereng.com
.. _`wikipedia_tcp`: http://en.wikipedia.org/wiki/Transmission_Control_Protocol
.. _`wikipedia_udp`: http://en.wikipedia.org/wiki/User_Datagram_Protocol
