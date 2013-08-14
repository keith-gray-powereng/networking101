.. Networking 101 documentation master file, created by
   sphinx-quickstart on Thu Jun 27 09:52:12 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========================================
Networking 101 - How the Internet Works!
========================================

Outline
=======

.. contents:: 
   :depth: 2

Introduction
============

History of SCADA
----------------

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

Network Layer Modeling
======================

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
~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~
* Data Unit: Frame
* Framing, Physical addressing, Error Control, Media Access Control
* Communication within the same network

Layer 3: Network Layer
~~~~~~~~~~~~~~~~~~~~~~
* Data Unit: Packet/Datagram
* Path determination and logical addressing
* Communication between networks aka Routing

Layer 4: Transport Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~
* Data Unit: Segments
* End-to-end connection, reliability and flow control

Layer 5: Session Layer
~~~~~~~~~~~~~~~~~~~~~~
* Data Unit: Data
* Interhost communication, managing sessions between applications

Layer 6: Presentation Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Data Unit: Data
* Data representation, encryption and decryption, convert machine dependent data to machine independent data

Layer 7: Application Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~
* Data Unit: Data
* Network process to application

TCP/IP Model
------------

* Layer 1: Link Layer
* Layer 2: Internet Layer
* Layer 3: Transport Layer
* Layer 4: Application layer

Layer 1: Link Layer
~~~~~~~~~~~~~~~~~~~~~~~
* Corresponds to OSI Model Layers 1 (Physical) and 2 (Data Link)
* Responsible for sending/receiving data on the local network

Layer 2: Internet Layer
~~~~~~~~~~~~~~~~~~~~~~~~
* Corresponds to OSI Model Layer 3 (Network)
* Responsible for sending/receiving data across 2 or more networks

Layer 3: Transport Layer
~~~~~~~~~~~~~~~~~~~~~~
* Corresponds to OSI Model Layer 4 (Transport)
* Responsible for sending/receiving data between hosts

Layer 4: Application Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~
* Corresponds to OSI Model Layers 5 (Session), 6 (Presentation), and 7 (Application)
* Responsible for sending/receiving data between applications
* Responsible for formatting and presenting data

Which Model?
------------

The most commonly used model today is the TCP/IP model and is what we will be exploring today.

Layer Details
=============

References
==========
* `wikipedia_osi_model`_
* `wikipedia_internet_model`_

.. _wikipedia_osi_model: http://en.wikipedia.org/wiki/OSI_model
.. _wikipedia_internet_model: http://en.wikipedia.org/wiki/Internet_protocol_suite
