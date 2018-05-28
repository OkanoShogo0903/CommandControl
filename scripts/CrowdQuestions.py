# -*- coding: utf-8 -*-
'''
; grammar name CrowdQuestions
; grammar tier High

$Main   = $crowdq
# call one's own function
$crowdq = How many $people are in the crowd?

# ???
$crowdq = How many people in the crowd are ($posppl | {gesture})?

# call one's own function
# equal "How many $people are in the crowd?"
$crowdq = Tell me the number of $people in the crowd

# call one's own function
$crowdq = Was the person $posprs a $gprsng?

# ???
$crowdq = Tell me if the person ($posprs | {gesture}) was a $gprsn?

# ???
$crowdq = Tell me how many people were wearing $color

$people = $appl | $gppl
$appl   = children | adults | elders
$gppl   = males | females | men | women | boys | girls
$posppl = $posprs
$posppl = standing or sitting
$posppl = standing or lying down
$posppl = sitting or lying down
$posprs = standing | sitting | lying down
$gprsn  = male | female | man | woman | boy | girl
$gprsng = male or female | man or woman | boy or girl
$color  = red | blue | white | black | green | yellow
'''
