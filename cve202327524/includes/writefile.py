#!/usr/bin/env python

"""
 * CVE-2023-27524
 * CVE-2023-27524 Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""


def writedata(output, data):
    with open(output, 'a') as file:
        file.write(data)
