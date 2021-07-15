PICTURES = '''
picture nmos
pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
pic_line list=0.75,1.1,2.5,0,-0.4,0.3
pic_line list=2,1.1,0,0.9
pic_pin i i xy=0,0 
pic_pin o o xy=4,0 
pic_pin g i xy=2,2 
end
picture nmos_vss
pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
pic_line list=0.75,1.1,2.5,0,-0.4,0.3
pic_line list=2,1.1,0,0.9
pic_line list=0,0,0,0.5,0,-1
pic_pin o o xy=4,0 
pic_pin g i xy=2,2 
end


picture pmos
pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
pic_line list=0.75,1.1,2.5,0,-0.4,0.3
pic_line list=2,1.9,2,2
pic_circle list=2,1.5,2.4,1.5
pic_pin i i xy=0,0 
pic_pin o o xy=4,0 
pic_pin g i xy=2,2 
end
picture pmos_vdd
pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
pic_line list=0.75,1.1,2.5,0,-0.4,0.3
pic_line list=2,1.9,2,2
pic_circle list=2,1.5,2.4,1.5
pic_line list=0,0,0,0.5,0,-1
pic_pin o o xy=4,0 
pic_pin g i xy=2,2 
end

picture input
  pic_line list=-2.5,-0.5,0,1,1.5,0,0.5,-0.5,-0.5,-0.5,-1.5,0
  pic_line list=-0.5,0,0.5,0
  pic_prop primitive xy=0,0
end
picture inout
  pic_line list=0,0,-0.5,0.5,-1,0,-0.5,-0.5,0.5,-0.5,1,0,0.5,0.5
  pic_prop primitive xy=0,0
end
picture output
  pic_line list=0.5,-0.5,0,1,1.5,0,0.5,-0.5,-0.5,-0.5,-1.5,0
  pic_line list=0,0,0.5,0
  pic_prop primitive xy=0,0
end
picture node
  pic_fcircle list=0,0,0.3,0
  pic_prop primitive xy=0,0
end
picture vcc
  pic_line list=0,0,0,0.5,1,0,-2,0
  pic_prop primitive xy=0,0
end
picture gnd
  pic_line list=0,0,0,-0.5,0.5,0,-0.5,-0.5,-0.5,0.5,0.5,0
  pic_prop primitive xy=0,0
end
picture cap
  pic_line list=1,3.9,0,-1.7
  pic_line list=1,1.8,0,-1.7
  pic_line list=0.3,2.2,1.4,0
  pic_line list=0.3,1.8,1.4,0
  pic_pin p b xy=1,0
  pic_pin n b xy=1,4
end
picture res
  pic_line list=1,4,0,-1.5
  pic_line list=1,1.5,0,-1.5
  pic_line list=1,2.5,-0.4,-0.1,0.8,-0.1,-0.8,-0.1,0.8,-0.1,-0.8,-0.1,0.8,-0.1,-0.8,-0.1,0.8,-0.1,-0.8,-0.1,0.4,-0.1
  pic_pin p b xy=1,0
  pic_pin n b xy=1,4
end

picture box 
pic_pin o o xy=4,1
pic_pin i i xy=0,1
pic_aline list=0,1,0.5,1
pic_aline list=3.5,1,4,1
pic_aline list=0.5,0,3.5,0 
pic_aline list=0.5,2,3.5,2 
pic_aline list=0.5,0,0.5,2
pic_aline list=3.5,0,3.5,2
end

picture circle 
pic_pin o o xy=4,1
pic_pin i i xy=0,1
pic_aline list=0,1,0.5,1
pic_aline list=3.5,1,4,1
pic_circle list=2.0,1.0,0.5,1.0
end

picture action
  pic_aline list=-0.7,-0.7,0.7,0.7
  pic_aline list=-0.7,0.7,0.7,-0.7
  pic_circle list=0,0,1,0
  pic_prop nonentity xy=0,0
end

picture arrow 
  pic_aline list=0,1.1,2,1.1,1.5,1.4
  pic_aline list=0,1,2.3,1
  pic_aline list=0,0.9,2,0.9,1.5,0.6
  pic_aline list=1.5,1.4,2.3,1,1.5,0.6
  pic_prop nonentity xy=0,0
end

picture sdgnd
  pic_aline list=-1.4,-1.6,1.4,-1.6
  pic_aline list=-1,-2,1,-2
  pic_aline list=-0.6,-2.4,0.6,-2.4
  pic_aline list=0,-1,2,-1,0,-3,-2,-1,0,-1,0,0
  pic_prop primitive xy=0,0
end
picture sdvdd
  pic_aline list=-1.8,2,1.6,2
  pic_aline list=-1.6,1,-1.4,1.4,-1,1.6,-0.4,1.4,0,1
  pic_aline list=0,0,0,1,0.6,0.6,1.2,0.6,1.6,1
  pic_prop primitive xy=0,0
end
picture anlogvdd
  pic_aline list=-1.8,1,-1.4,1.4,-0.6,1.4,0,1
  pic_aline list=0,0,0,1,0.6,0.6,1.2,0.6,1.6,1
  pic_prop primitive xy=0,0
end
picture anloggnd
  pic_aline list=0,-0.6,0,0
  pic_aline list=-0.2,-1.8,0.2,-1.8
  pic_aline list=-0.8,-1.4,0.8,-1.4
  pic_aline list=-1.4,-1,1.4,-1
  pic_aline list=-2,-0.6,0,-0.6,2,-0.6
  pic_prop primitive xy=0,0
end
picture agnd
  pic_aline list=0,-0.6,0,0
  pic_aline list=-0.2,-1.8,0.2,-1.8
  pic_aline list=-0.8,-1.4,0.8,-1.4
  pic_aline list=-1.4,-1,1.4,-1
  pic_aline list=-2,-0.6,0,-0.6,2,-0.6
  pic_prop primitive xy=0,0
end
picture avcc
  pic_aline list=-1.8,1,-1.4,1.4,-0.6,1.4,0,1
  pic_aline list=0,0,0,1,0.6,0.6,1.2,0.6,1.6,1
  pic_prop primitive xy=0,0
end
picture note
  pic_prop nonentity xy=0,0
  pic_geom frect list=0,0,1,1
end
picture corner_logo
pic_line list=0,0,0,5,8,0
pic_line list=0.5,0.5,0,4.0,7,0
end
picture logo_base
  pic_line list=0,0,20,0,0,8,-20,0,0,-8
  pic_text Ilia free xy=0.5,1.5
  pic_text Date  : xy=0.5,3.0
  pic_text Eng   : xy=0.5,4.5
  pic_text Block : xy=0.5,6.0
end
picture logo_s
  pic_line list=0,0,54,0,0,42,-54,0,0,-42
  pic_prop nonentity xy=0,0
  pic_sub company xy=2,2
end
picture logo_a
  pic_line list=0,0,108,0,0,84,-108,0,0,-84
  pic_prop nonentity xy=0,0
  pic_sub company xy=2,2
end
picture logo
  pic_line list=0,0,90,0,0,70,-90,0,0,-70
  pic_prop nonentity xy=0,0
  pic_sub company xy=2,2
end
picture logo_a
  pic_line list=0,0,108,0,0,84,-108,0,0,-84
  pic_prop nonentity xy=0,0
  pic_sub company xy=2,2
end
picture logo_b
  pic_line list=0,0,130,0,0,101,-130,0,0,-101
  pic_prop nonentity xy=0,0
  pic_sub company xy=2,2
end
picture focus_node
  pic_aline list=2.14,1.12,2.2,0.7
  pic_aline list=2.2,2.86,2.62,3.1
  pic_aline list=0.22,2.68,0.46,2.44
  pic_aline list=2.68,1.42,2.92,0.820001
  pic_aline list=2.92,2.02,3.28,2.02
  pic_aline list=0.46,1.72,0.7,1.6
  pic_aline list=0.52,0.7,0.820001,0.88
  pic_aline list=0.7,2.38,1.78,2.8,2.38,2.74,2.86,2.44,2.86,1.84,2.5,1.42,1.72,1.06,1.12,1.06,0.94,1.6,0.820001,1.84,1.72,2.02,2.08,2.02,2.38,1.78,2.08,1.42,1.66,1.3,1.42,1.54,1.66,1.84,1.96,1.8999
  pic_aline list=0.820001,0.5,1.42,0.88
  pic_aline list=0.94,3.16,0.76,2.8
  pic_fcircle list=0,0,1,0
  pic_prop primitive xy=0,0
  pic_prop arrive xy=5,0
  pic_prop ready xy=5,2
  pic_prop cout xy=5,4
end
picture pv_array
  pic_line list=0,0,0,4,2,0,0,-4,-2,0
  pic_line list=0,4,1,-1,1,1
  pic_text PV xy=0.3,2
  pic_text arr xy=0.1,1
  pic_pin p o xy=1,4
  pic_pin n i xy=1,0
end
picture nmos
  pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
  pic_line list=0.75,1.1,2.5,0,-0.4,0.3
  pic_line list=2,1.1,0,0.9
  pic_pin i i xy=0,0
  pic_pin o o xy=4,0
  pic_pin g i xy=2,2
end
picture nmoshv
  pic_aline list=0.75,1.1,3.25,1.1
  pic_aline list=2,1.3,2,3
  pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
  pic_line list=0.75,1.3,2.5,0,-0.4,0.3
  pic_pin i i xy=0,0
  pic_pin o o xy=4,0
  pic_pin g i xy=2,3
end
picture nmoshv_vss
  pic_aline list=0.75,1.1,3.25,1.1
  pic_aline list=2,1.3,2,3
  pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
  pic_line list=0.75,1.3,2.5,0,-0.4,0.3
  pic_line list=0,0,0,0.5,0,-1
  pic_pin o o xy=4,0
  pic_pin g i xy=2,3
end
picture nmos4_share
  pic_aline list=3.1,0,3.1,0.75
  pic_aline list=2.9,0,2.9,0.75
  pic_aline list=2,-1,2,0.75,1.75,0.5,2.25,0.5,2,0.75
  pic_sub nmos xy=0,0
  pic_pin s b xy=2,-1
end
picture pmos4_share
  pic_aline list=3.1,0,3.1,0.75
  pic_aline list=2.9,0,2.9,0.75
  pic_aline list=2,-1,2,0.75,1.75,0.5,2.25,0.5,2,0.75
  pic_sub pmos xy=0,0
  pic_pin s b xy=2,-1
end
picture nmos4
  pic_aline list=2,-1,2,0.75,1.75,0.5,2.25,0.5,2,0.75
  pic_sub nmos xy=0,0
  pic_pin s b xy=2,-1
end
picture nmos4_io
  pic_aline list=2,-1,2,0.75,1.75,0.5,2.25,0.5,2,0.75
  pic_sub nmos_io xy=0,0
  pic_pin s b xy=2,-1
end
picture nmos_share
  pic_aline list=3.1,0,3.1,0.75
  pic_aline list=2.9,0,2.9,0.75
  pic_sub nmos xy=0,0
end
picture pmos_share
  pic_aline list=3.1,0,3.1,0.75
  pic_aline list=2.9,0,2.9,0.75
  pic_sub pmos xy=0,0
end
picture pmos4
  pic_aline list=2,-1,2,0.75,1.75,0.5,2.25,0.5,2,0.75
  pic_sub pmos xy=0,0
  pic_pin s b xy=2,-1
end
picture pmos4_io
  pic_aline list=2,-1,2,0.75,1.75,0.5,2.25,0.5,2,0.75
  pic_sub pmos_io xy=0,0
  pic_pin s b xy=2,-1
end
picture pmos
  pic_aline list=2,1.9,2,2.0
  pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
  pic_line list=0.75,1.1,2.5,0,-0.4,0.3
  pic_circle list=2,1.5,2.4,1.5
  pic_pin i i xy=0,0
  pic_pin o o xy=4,0
  pic_pin g i xy=2,2
end
picture pmoshv
  pic_aline list=0.75,1.1,3.25,1.1
  pic_aline list=2,2.1,2,3.0
  pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
  pic_line list=0.75,1.3,2.5,0,-0.4,0.3
  pic_circle list=2,1.7,2.4,1.7
  pic_pin i i xy=0,0
  pic_pin o o xy=4,0
  pic_pin g i xy=2,3
end
picture pmoshv_vdd
  pic_aline list=0.75,1.1,3.25,1.1
  pic_aline list=2,2.1,2,3.0
  pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
  pic_line list=0.75,1.3,2.5,0,-0.4,0.3
  pic_circle list=2,1.7,2.4,1.7
  pic_line list=0,0,0,0.5,0,-1
  pic_pin o o xy=4,0
  pic_pin g i xy=2,3
end

picture nc
  pic_aline list=-0.5,-0.5,0.5,0.5
  pic_aline list=-0.5,0.5,0.5,-0.5
  pic_prop primitive xy=0,0
end
picture antenna
  pic_aline list=0,0,0.5,0,0.8,0.3,1.2,0,0.8,-0.3,0.5,0
  pic_pin i i xy=0,0
end
picture antennab
  pic_aline list=0,0,0.5,0
  pic_circle list=1,0,1.5,0
  pic_prop primitive xy=0,0
end
picture diode
  pic_aline list=-2,4,2,4
  pic_aline list=0,0,0,1
  pic_aline list=0,4,2,1,-2,1,0,4,0,5
  pic_pin p i xy=0,0
  pic_pin n o xy=0,5
end
picture isource
  pic_aline list=0,0,0,1
  pic_aline list=0,5,0,4
  pic_aline list=-1.5,1.2,-1.3,1,-1.1,1.2
  pic_aline list=-1.3,1,-1.3,3
  pic_circle list=0,2,0,3
  pic_circle list=0,3,0,4
  pic_pin p b xy=0,5
  pic_pin n b xy=0,0
end
picture vsource
  pic_aline list=0,0,0,1
  pic_aline list=0,3.5,0,2.5
  pic_aline list=-2,2.5,2,2.5
  pic_aline list=-1,2,1,2
  pic_aline list=-2,1.5,2,1.5
  pic_aline list=-1,1,1,1
  pic_pin p b xy=0,3.5
  pic_pin n b xy=0,0
end
picture transformer
  pic_line list=0.2,2.2,3,0
  pic_line list=0.2,2.4,3,0
  pic_line list=0.2,2.6,3,0
  pic_sub coil xy=0,0
  pic_sub coil xy=0,3
  pic_pin p0 b xy=0.0,0.5
  pic_pin p1 b xy=3.0,0.5
  pic_pin s0 b xy=0.0,3.5
  pic_pin s1 b xy=3.0,3.5
end

picture coil
pic_pin n i xy=0.0,0.5
pic_pin p o xy=3.0,0.5
pic_aline list=0.00,0.54,0.48,0.54
pic_aline list=3.00,0.54,2.65,0.54
pic_aline list=0.48,0.54,0.65,0.86
pic_aline list=0.65,0.86,0.87,1.16
pic_aline list=0.87,1.16,1.14,1.32
pic_aline list=1.33,1.25,1.44,0.96
pic_aline list=1.49,0.48,1.49,0.48
pic_aline list=1.44,0.96,1.49,0.48
pic_aline list=2.22,1.08,2.31,0.81
pic_aline list=2.34,0.46,2.30,0.13
pic_aline list=1.79,0.17,1.75,0.52
pic_aline list=0.89,0.13,0.77,0.39
pic_aline list=0.89,0.71,1.13,1.06
pic_aline list=1.49,0.48,1.39,0.20
pic_aline list=1.39,0.20,1.13,0.08
pic_aline list=1.90,1.25,2.22,1.08
pic_aline list=2.31,0.81,2.34,0.46
pic_aline list=1.13,1.06,1.57,1.29
pic_aline list=1.57,1.29,1.90,1.25
pic_aline list=2.50,0.91,2.65,0.54
pic_aline list=2.27,1.16,2.50,0.91
pic_aline list=1.80,0.87,2.03,1.12
pic_aline list=1.75,0.52,1.80,0.87
pic_aline list=2.30,0.13,2.06,0.00
pic_aline list=0.77,0.39,0.89,0.71
pic_aline list=1.13,0.08,0.89,0.13
pic_aline list=1.14,1.32,1.33,1.25
pic_aline list=2.03,1.12,2.27,1.16
pic_aline list=2.06,0.00,1.79,0.17
end

picture cmos
  pic_aline list=2,-0.6,2,-2
  pic_aline list=2,1.4,2,2
  pic_aline list=0.5,-1.2,3.5,0
  pic_aline list=3.5,-1.2,0.5,0
  pic_aline list=0.5,1.2,3.5,0
  pic_aline list=3.5,1.2,0.5,0
  pic_aline list=3.5,-1.2,3.5,1.2
  pic_aline list=0.5,-1.2,0.5,1.2
  pic_aline list=3.5,0,4,0
  pic_aline list=0.5,0,0,0
  pic_aline list=2.4,-0.4,2.4,0.4,3.4,0,2.4,-0.4
  pic_circle list=2,1,2.4,1
  pic_pin i i xy=0,0
  pic_pin o o xy=4,0
  pic_pin cb i xy=2,2
  pic_pin c_b i xy=2,2
  pic_pin c_ i xy=2,2
  pic_pin c i xy=2,-2
  pic_pin gp i xy=2,2
  pic_pin gn i xy=2,-2
end
picture bcmos
  pic_aline list=2,-0.6,2,-2
  pic_aline list=2,1.4,2,2
  pic_aline list=0.5,-1.2,3.5,0
  pic_aline list=3.5,-1.2,0.5,0
  pic_aline list=0.5,1.2,3.5,0
  pic_aline list=3.5,1.2,0.5,0
  pic_aline list=3.5,-1.2,3.5,1.2
  pic_aline list=0.5,-1.2,0.5,1.2
  pic_aline list=3.5,0,4,0
  pic_aline list=0.5,0,0,0
  pic_circle list=2,1,2.4,1
  pic_pin i i xy=0,0
  pic_pin o o xy=4,0
  pic_pin c_b i xy=2,2
  pic_pin cb i xy=2,2
  pic_pin c_ i xy=2,2
  pic_pin c i xy=2,-2
end
picture bnmos
  pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
  pic_line list=0.75,1.1,2.5,0
  pic_line list=2,1.1,0,0.9
  pic_pin i i xy=0,0
  pic_pin o o xy=4,0
  pic_pin g i xy=2,2
end
picture bpmos
  pic_line list=0,0,0.75,0,0,0.75,2.5,0,0,-0.75,0.75,0
  pic_line list=0.75,1.1,2.5,0
  pic_line list=2,1.9,0,0.5
  pic_circle list=2,1.5,2.4,1.5
  pic_pin i i xy=0,0
  pic_pin o o xy=4,0
  pic_pin g i xy=2,2
end
picture company
  pic_prop nonentity xy=0,0
  pic_text Zdraw:ilia@mac.com.054-4927322 xy=-3,0
end
picture ilia
  pic_sub signature_of_ilia xy=0,0
end
picture signature_of_ilia
  pic_aline list=4.4,1.6,4.6,1.4
  pic_aline list=1.2,4.2,2.2,4.2
  pic_aline list=1.0,2.8,2.0,2.8
  pic_aline list=1.4,2.8,1.8,4.2
  pic_aline list=3.4,2.8,3.6,3.6
  pic_aline list=4.2,3.2,4.6,3.2
  pic_aline list=4.0,2.8,4.4,3.6,4.6,2.8
  pic_aline list=2.8,3.6,2.4,2.8,2.8,2.8
  pic_aline list=7.0,1.6,7.0,1.0,6.6,1.0,6.2,1.0,6.2,0.2,6.6,0.0,7.0,0.2
  pic_aline list=4.0,1.6,4.2,1.0,4.2,0.2,4.0,0.0,3.6,0.0
  pic_aline list=5.0,1.6,5.4,1.6,5.8,1.4,5.8,1.0,5.8,0.4,5.6,0.0
  pic_aline list=2.2,0.0,2.4,0.4,2.8,0.0,3.2,0.0,3.2,0.6,3.0,1.2,2.6,1.6,2.0,1.2,2.0,0.6
  pic_aline list=1.2,0.6,1.0,0.6,0.8,0.2,1.0,0.0,1.2,0.0,1.4,0.4,1.4,1.2,1.8,2.0,3.2,2.2
  pic_aline list=0.6,1.8,0.2,1.6,0.0,1.2,-0.2,0.8,0.0,0.2,0.4,0.0,0.6,0.4,0.4,0.8,0.2,0.8
end
picture transmission_line
  pic_aline list=-1,2,1,2
  pic_aline list=7.6,2,9,2
  pic_aline list=4,-0.8,4,0
  pic_aline list=3.4,-0.8,4.6,-0.8
  pic_aline list=3.6,-1,4.4,-1
  pic_aline list=4.2,-1.2,3.8,-1.2,4,-1.4,4.2,-1.2
  pic_aline list=1,0,7,0,7.4,0.8,7.6,2,7.4,3.2,7,4,1,4,1.4,3.2,1.6,2,1.4,0.8,1,0,0.6,0.8,0.4,2,0.6,3.2,1,4
  pic_prop z0 xy=2,7
  pic_prop td xy=2,5
  pic_pin p b xy=-1,2
  pic_pin n b xy=9,2
end
picture rcload
  pic_aline list=3,4,3.6,4
  pic_aline list=2.4,4,3,4,3,5
  pic_aline list=2.4,3.6,3,3.6,3.6,3.6
  pic_aline list=3,2.8,3.4,2.8,3,2.4,2.6,2.8,3,2.8,3,3.6
  pic_aline list=0,5,3,5,4,5,4.4,5.2,4.6,4.8,4.8,5.2,5,4.8,5.2,5.2,5.6,5,7,5
  pic_prop geom xy=2,7
  pic_prop layer xy=2,6
  pic_pin p b xy=0,5
  pic_pin n b xy=7,5
end
picture and2
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=5.0,2,6,2
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_aline list=3.5,0.5,4,0.7,4.6,1.1,5,2,4.6,2.8,4.0,3.3,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
end
picture and3
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=0,2,1,2
  pic_aline list=5.0,2,6,2
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_aline list=3.5,0.5,4,0.7,4.6,1.1,5,2,4.6,2.8,4.0,3.3,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i1 i xy=0,3
end
picture andi3
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=0,2,1,2
  pic_aline list=5.0,2,6,2
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_aline list=3.5,0.5,4,0.7,4.6,1.1,5,2,4.6,2.8,4.0,3.3,3.5,3.5
  pic_circle list=0.8,1,1.0,1
  pic_pin o1 o xy=6,2
  pic_pin i3 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i1 i xy=0,1
end
picture and4
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=0,2,1,2
  pic_aline list=5,2,6,2
  pic_aline list=0,0,1,0,1,1
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_geom arc list=3.5,0.5,3.5,2,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
end
picture and5
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=0,2,1,2
  pic_aline list=5,2,6,2
  pic_aline list=0,0,1,0,1,1
  pic_aline list=0,4,1,4,1,3.5
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_geom arc list=3.5,0.5,3.5,2,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,4
  pic_pin i2 i xy=0,3
  pic_pin i3 i xy=0,2
  pic_pin i4 i xy=0,1
  pic_pin i5 i xy=0,0
end
picture inv
  pic_aline list=0,2,0.5,2,0.5,0.5,3,2,0.5,3.5,0.5,2
  pic_aline list=3.8,2,4,2
  pic_circle list=3.4,2,3,2
  pic_pin o1 o xy=4,2
  pic_pin i1 i xy=0,2
end
picture buf
  pic_aline list=0,2,0.5,2,0.5,0.5,3,2,0.5,3.5,0.5,2
  pic_aline list=3.0,2,4,2
  pic_pin o1 o xy=4,2
  pic_pin i1 i xy=0,2
end
picture nand2
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=5.8,2,6,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_aline list=3.5,0.5,4,0.7,4.8,1.1,5,2,4.8,2.8,4.0,3.3,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
end
picture nandi2
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=5.8,2,6,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_aline list=3.5,0.5,4,0.7,4.8,1.1,5,2,4.8,2.8,4.0,3.3,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i2 i xy=0,1
  pic_circle list=1.0,1,0.6,1.0
  pic_pin i1 i xy=0,3
end
picture andi2
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=5.0,2,5.5,2
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_aline list=3.5,0.5,4,0.7,4.8,1.1,5,2,4.8,2.8,4.0,3.3,3.5,3.5
  pic_pin o1 o xy=5.5,2
  pic_pin i2 i xy=0,1
  pic_circle list=1.0,1,0.6,1.0
  pic_pin i1 i xy=0,3
end

picture nand3
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=0,2,1,2
  pic_aline list=5.8,2,6,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=1.8,2.9,1.5,2.9
#  pic_geom arc list=3.5,0.5,3.5,2,3.5,3.5
  pic_aline list=3.5,0.5,4,0.7,4.5,1.1,5,2,4.5,2.8,4.0,3.3,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i3 i xy=0,1
  pic_pin i2 i xy=0,2
  pic_pin i1 i xy=0,3
end
picture nand4
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=0,2,1,2
  pic_aline list=0,0,1,0,1,0.5
  pic_aline list=5.8,2,6,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_geom arc list=3.5,0.5,3.5,2,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i4 i xy=0,0
  pic_pin i3 i xy=0,1
  pic_pin i2 i xy=0,2
  pic_pin i1 i xy=0,3
end
picture nand5
  pic_aline list=0,1,1,1,1,0.5,3.5,0.5
  pic_aline list=0,3,1,3,1,3.5,3.5,3.5
  pic_aline list=1,1,1,3
  pic_aline list=0,2,1,2
  pic_aline list=0,0,1,0,1,0.5
  pic_aline list=0,4,1,4,1,3.5
  pic_aline list=5.8,2,6,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=1.8,2.9,1.5,2.9
  pic_geom arc list=3.5,0.5,3.5,2,3.5,3.5
  pic_pin o1 o xy=6,2
  pic_pin i5 i xy=0,0
  pic_pin i4 i xy=0,1
  pic_pin i3 i xy=0,2
  pic_pin i2 i xy=0,3
  pic_pin i1 i xy=0,4
end
picture nor2
  pic_aline list=5.8,2,6,2
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
end
picture nor3
  pic_aline list=5.8,2,6,2
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=0,2,1.4,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i3 i xy=0,1
  pic_pin i2 i xy=0,2
  pic_pin i1 i xy=0,3
end
picture nor4
  pic_aline list=5.8,2,6,2
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=0,2,1.4,2
  pic_aline list=0,0,1,0,1,0.5
  pic_circle list=5.4,2,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i4 i xy=0,0
  pic_pin i3 i xy=0,1
  pic_pin i2 i xy=0,2
  pic_pin i1 i xy=0,3
end
picture or2
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5.0,2,6,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
end
picture or3
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5.0,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
end
picture or7
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=1,0.5,1,0,0,0
  pic_aline list=1,0,1,-1,0,-1
  pic_aline list=1,-1,1,-2,0,-2
  pic_aline list=1,-2,1,-3,0,-3
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
  pic_pin i5 i xy=0,-1
  pic_pin i6 i xy=0,-2
  pic_pin i7 i xy=0,-3
end
picture or6
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=1,0.5,1,0,0,0
  pic_aline list=1,0,1,-1,0,-1
  pic_aline list=1,-1,1,-2,0,-2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
  pic_pin i5 i xy=0,-1
  pic_pin i6 i xy=0,-2
end
picture or5
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=1,0.5,1,0,0,0
  pic_aline list=1,0,1,-1,0,-1
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
  pic_pin i5 i xy=0,-1
end
picture or4
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=1,0.5,1,0,0,0
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
end
picture xor
  pic_aline list=5,2,6,2
  pic_aline list=0,1,1,1
  pic_aline list=0.6,0.4,1,1,1,3
  pic_aline list=0.6,3.6,1,3,0,3
  pic_aline list=3.8,3.4,2.8,3.6,1,3.6,1.4,3,1.4,1,1,0.4,2.8,0.4,3.8,0.6,4.4,1.2,5,2,4.4,2.8,3.8,3.4
  pic_fcircle list=2.0,3.0,2.3,3.0
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
  pic_pin o o xy=6,2
end
picture xnor2
  pic_sub xnor xy=0,0
end
picture xor2
  pic_aline list=5,2,6,2
  pic_aline list=0,1,1,1
  pic_aline list=0.6,0.4,1,1,1,3
  pic_aline list=0.6,3.6,1,3,0,3
  pic_aline list=3.8,3.4,2.8,3.6,1,3.6,1.4,3,1.4,1,1,0.4,2.8,0.4,3.8,0.6,4.4,1.2,5,2,4.4,2.8,3.8,3.4
  pic_fcircle list=2.0,3.0,2.3,3.0
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
  pic_pin o o xy=6,2
end

picture xnor
  pic_aline list=5.8,2,6,2
  pic_aline list=0,1,1,1
  pic_aline list=0.6,0.4,1,1,1,3
  pic_aline list=0.6,3.6,1,3,0,3
  pic_aline list=3.8,3.4,2.8,3.6,1,3.6,1.4,3,1.4,1,1,0.4,2.8,0.4,3.8,0.6,4.4,1.2,5,2,4.4,2.8,3.8,3.4
  pic_circle list=5.4,2.0,5.0,2.0
  pic_fcircle list=2.0,3.0,2.3,3.0
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
  pic_pin o o xy=6,2
end
picture nmux
  pic_aline list=3.8,2,4,2
  pic_aline list=2,3,2,4
  pic_aline list=0,3,0.6,3
  pic_aline list=0,1,0.6,1
  pic_aline list=3,2.4,0.6,3.6,0.6,0.4,3,1.6,3,2.4
  pic_circle list=3.4,2.0,3.0,2.0
  pic_fcircle list=1.2,2.6,1.5,2.6
  pic_pin i0 i xy=0,3
  pic_pin i1 i xy=0,1
  pic_pin s i xy=2,4
  pic_pin o o xy=4,2
end
picture mux
  pic_aline list=3.0,2,4,2
  pic_aline list=2,3,2,4
  pic_aline list=0,3,0.6,3
  pic_aline list=0,1,0.6,1
  pic_aline list=3,2.4,0.6,3.6,0.6,0.4,3,1.6,3,2.4
  pic_fcircle list=1.2,2.6,1.5,2.6
  pic_pin i0 i xy=0,3
  pic_pin i1 i xy=0,1
  pic_pin s i xy=2,4
  pic_pin o o xy=4,2
end
  pic_pin i1 i xy=0,4
end
picture nor2
  pic_aline list=5.8,2,6,2
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
end
picture nor3
  pic_aline list=5.8,2,6,2
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=0,2,1.4,2
  pic_circle list=5.4,2,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i3 i xy=0,1
  pic_pin i2 i xy=0,2
  pic_pin i1 i xy=0,3
end
picture nor4
  pic_aline list=5.8,2,6,2
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=0,2,1.4,2
  pic_aline list=0,0,1,0,1,0.5
  pic_circle list=5.4,2,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i4 i xy=0,0
  pic_pin i3 i xy=0,1
  pic_pin i2 i xy=0,2
  pic_pin i1 i xy=0,3
end
picture or2
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5.0,2,6,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
end
picture or3
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5.0,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
end
picture or7
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=1,0.5,1,0,0,0
  pic_aline list=1,0,1,-1,0,-1
  pic_aline list=1,-1,1,-2,0,-2
  pic_aline list=1,-2,1,-3,0,-3
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
  pic_pin i5 i xy=0,-1
  pic_pin i6 i xy=0,-2
  pic_pin i7 i xy=0,-3
end
picture or6
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=1,0.5,1,0,0,0
  pic_aline list=1,0,1,-1,0,-1
  pic_aline list=1,-1,1,-2,0,-2
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
  pic_pin i5 i xy=0,-1
  pic_pin i6 i xy=0,-2
end
picture or5
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=1,0.5,1,0,0,0
  pic_aline list=1,0,1,-1,0,-1
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
  pic_pin i5 i xy=0,-1
end
picture or4
  pic_aline list=0,1,1.2,1,1,0.5,3,0.5
  pic_aline list=0,3,1.2,3,1,3.5,3,3.5
  pic_aline list=1.2,1,1.3,1.4,1.4,2,1.3,2.6,1.2,3
  pic_aline list=5,2,6,2
  pic_aline list=0,2,1.2,2
  pic_aline list=3,3.5,3.5,3.4,4,3.1,4.5,2.6,5,2
  pic_aline list=3,0.5,3.5,0.6,4,0.9,4.5,1.4,5,2
  pic_aline list=1,0.5,1,0,0,0
  pic_fcircle list=2.0,2.9,1.7,2.9
  pic_pin o1 o xy=6,2
  pic_pin i1 i xy=0,3
  pic_pin i2 i xy=0,2
  pic_pin i3 i xy=0,1
  pic_pin i4 i xy=0,0
end
picture xor
  pic_aline list=5,2,6,2
  pic_aline list=0,1,1,1
  pic_aline list=0.6,0.4,1,1,1,3
  pic_aline list=0.6,3.6,1,3,0,3
  pic_aline list=3.8,3.4,2.8,3.6,1,3.6,1.4,3,1.4,1,1,0.4,2.8,0.4,3.8,0.6,4.4,1.2,5,2,4.4,2.8,3.8,3.4
  pic_fcircle list=2.0,3.0,2.3,3.0
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
  pic_pin o o xy=6,2
end
picture xnor2
  pic_sub xnor xy=0,0
end
picture xor2
  pic_aline list=5,2,6,2
  pic_aline list=0,1,1,1
  pic_aline list=0.6,0.4,1,1,1,3
  pic_aline list=0.6,3.6,1,3,0,3
  pic_aline list=3.8,3.4,2.8,3.6,1,3.6,1.4,3,1.4,1,1,0.4,2.8,0.4,3.8,0.6,4.4,1.2,5,2,4.4,2.8,3.8,3.4
  pic_fcircle list=2.0,3.0,2.3,3.0
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
  pic_pin o o xy=6,2
end

picture xnor
  pic_aline list=5.8,2,6,2
  pic_aline list=0,1,1,1
  pic_aline list=0.6,0.4,1,1,1,3
  pic_aline list=0.6,3.6,1,3,0,3
  pic_aline list=3.8,3.4,2.8,3.6,1,3.6,1.4,3,1.4,1,1,0.4,2.8,0.4,3.8,0.6,4.4,1.2,5,2,4.4,2.8,3.8,3.4
  pic_circle list=5.4,2.0,5.0,2.0
  pic_fcircle list=2.0,3.0,2.3,3.0
  pic_pin i2 i xy=0,1
  pic_pin i1 i xy=0,3
  pic_pin o o xy=6,2
end
picture nmux
  pic_aline list=3.8,2,4,2
  pic_aline list=2,3,2,4
  pic_aline list=0,3,0.6,3
  pic_aline list=0,1,0.6,1
  pic_aline list=3,2.4,0.6,3.6,0.6,0.4,3,1.6,3,2.4
  pic_circle list=3.4,2.0,3.0,2.0
  pic_fcircle list=1.2,2.6,1.5,2.6
  pic_pin i0 i xy=0,3
  pic_pin i1 i xy=0,1
  pic_pin s i xy=2,4
  pic_pin o o xy=4,2
end
picture mux2
  pic_aline list=3.0,2,4,2
  pic_aline list=2,3,2,4
  pic_aline list=0,3,0.6,3
  pic_aline list=0,1,0.6,1
  pic_aline list=3,2.4,0.6,3.6,0.6,0.4,3,1.6,3,2.4
  pic_fcircle list=1.2,2.6,1.5,2.6
  pic_pin i0 i xy=0,3
  pic_pin i1 i xy=0,1
  pic_pin s i xy=2,4
  pic_pin o o xy=4,2
end
picture mux4
  pic_aline list=3.0,2,4,2
  pic_aline list=2,3,2,4
  pic_aline list=2.8,2.6,2.8,4
  pic_aline list=0,3.5,0.6,3.5
  pic_aline list=0,2.5,0.6,2.5
  pic_aline list=0,1.5,0.6,1.5
  pic_aline list=0,0.5,0.6,0.5
  pic_aline list=3,2.4,0.6,3.6,0.6,0.4,3,1.6,3,2.4
  pic_fcircle list=1.2,2.6,1.5,2.6
  pic_pin i0 i xy=0,0.5
  pic_pin i1 i xy=0,1.5
  pic_pin i2 i xy=0,2.5
  pic_pin i3 i xy=0,3.5
  pic_pin s0 i xy=2,4
  pic_pin s1 i xy=2.8,4
  pic_pin o o xy=4,2
end

picture gatedclk
    pic_aline list=0.5,0.5,0.5,4.5,4.5,4.5,4.5,0.5,0.5,0.5
    pic_pin en i xy=0,2.3
    pic_text en xy=0.8,2.2
    pic_aline list=0,2.3,0.5,2.3
    pic_pin q o xy=5,3.8
    pic_text q xy=4.0,3.4
    pic_aline list=4.5,3.8,5.0,3.8
    pic_pin ck i xy=2.6,0
    pic_aline list=2.6,0,2.6,0.5
    pic_text ck xy=2.4,1.0
    pic_aline list=2.4,0.5,2.6,0.9,2.8,0.5
    pic_text gatedclk xy=0.7,4.6
end

picture dffr
pic_pin rn i xy=1.3,0.0
pic_pin ck i xy=0.0,2.6
pic_pin d i xy=0.0,1.5
pic_pin q o xy=4.0,2.7
pic_pin qn o xy=3.9,1.3
pic_aline list=0.41,0.72,1.24,0.72
pic_aline list=1.24,0.72,3.11,0.72
pic_aline list=3.11,0.72,3.11,1.22
pic_aline list=3.11,2.68,4.00,2.68
pic_aline list=3.11,2.68,3.11,3.13
pic_aline list=3.11,3.13,0.41,3.13
pic_aline list=1.24,0.72,1.09,0.60
pic_aline list=0.41,2.60,0.41,0.72
pic_aline list=3.38,1.03,3.55,1.07
pic_aline list=3.11,1.38,3.24,1.51
pic_aline list=3.24,1.51,3.40,1.55
pic_aline list=3.40,1.55,3.57,1.51
pic_aline list=3.38,1.03,3.22,1.09
pic_aline list=1.57,0.49,1.53,0.33
pic_aline list=1.32,0.25,1.32,0.00
pic_aline list=0.02,2.60,0.41,2.60
pic_aline list=1.13,0.29,1.32,0.25
pic_aline list=0.43,1.46,0.00,1.46
pic_aline list=0.41,3.13,0.41,2.60
pic_aline list=1.32,0.25,1.53,0.33
pic_aline list=1.55,0.62,1.57,0.49
pic_aline list=3.11,1.22,3.11,2.68
pic_aline list=1.42,0.72,1.55,0.62
pic_aline list=3.65,1.38,3.65,1.20
pic_aline list=3.57,1.51,3.65,1.38
pic_aline list=3.65,1.30,3.94,1.30
pic_aline list=3.22,1.09,3.11,1.22
pic_aline list=3.65,1.20,3.55,1.07
pic_aline list=1.09,0.43,1.13,0.29
pic_aline list=1.09,0.43,1.09,0.60
pic_text ck xy=0.6,2.5
pic_text d xy=0.5,1.3
pic_text q xy=2.7,2.4
pic_text dffr xy=0.5,3.3
pic_text rn xy=1.0,0.8
pic_text qn xy=2.3,1.1
end

picture dffs
pic_pin sn i xy=1.3,0.0
pic_pin ck i xy=0.0,2.6
pic_pin d i xy=0.0,1.5
pic_pin q o xy=4.0,2.7
pic_pin qn o xy=3.9,1.3
pic_aline list=0.41,0.72,1.24,0.72
pic_aline list=1.24,0.72,3.11,0.72
pic_aline list=3.11,0.72,3.11,1.22
pic_aline list=3.11,2.68,4.00,2.68
pic_aline list=3.11,2.68,3.11,3.13
pic_aline list=3.11,3.13,0.41,3.13
pic_aline list=1.24,0.72,1.09,0.60
pic_aline list=0.41,2.60,0.41,0.72
pic_aline list=3.38,1.03,3.55,1.07
pic_aline list=3.11,1.38,3.24,1.51
pic_aline list=3.24,1.51,3.40,1.55
pic_aline list=3.40,1.55,3.57,1.51
pic_aline list=3.38,1.03,3.22,1.09
pic_aline list=1.57,0.49,1.53,0.33
pic_aline list=1.32,0.25,1.32,0.00
pic_aline list=0.02,2.60,0.41,2.60
pic_aline list=1.13,0.29,1.32,0.25
pic_aline list=0.43,1.46,0.00,1.46
pic_aline list=0.41,3.13,0.41,2.60
pic_aline list=1.32,0.25,1.53,0.33
pic_aline list=1.55,0.62,1.57,0.49
pic_aline list=3.11,1.22,3.11,2.68
pic_aline list=1.42,0.72,1.55,0.62
pic_aline list=3.65,1.38,3.65,1.20
pic_aline list=3.57,1.51,3.65,1.38
pic_aline list=3.65,1.30,3.94,1.30
pic_aline list=3.22,1.09,3.11,1.22
pic_aline list=3.65,1.20,3.55,1.07
pic_aline list=1.09,0.43,1.13,0.29
pic_aline list=1.09,0.43,1.09,0.60
pic_text ck xy=0.6,2.5
pic_text d xy=0.5,1.3
pic_text q xy=2.7,2.4
pic_text dffs xy=0.5,3.3
pic_text sn xy=1.0,0.8
pic_text qn xy=2.3,1.1
end


picture latchr
    pic_aline list=0.5,0.5,0.5,4.5,4.5,4.5,4.5,0.5,0.5,0.5
    pic_text latchr xy=0.7,4.6

    pic_pin d i xy=0,2.3
    pic_text d xy=0.8,2.2
    pic_aline list=0,2.3,0.5,2.3

    pic_pin q o xy=5.1,3.8
    pic_text q xy=4.0,3.6
    pic_aline list=4.5,3.8,5.1,3.8

    pic_pin qn o xy=5.1,3.0
    pic_text qn xy=3.8,2.8
    pic_aline list=4.9,3.0,5.1,3.0
    pic_circle list=4.7,3.0,4.5,3.0

    pic_pin en i xy=2.6,0
    pic_aline list=2.6,0,2.6,0.5
    pic_text en xy=2.4,1.0
    pic_aline list=2.4,0.5,2.6,0.9,2.8,0.5

    pic_pin rn i xy=1.6,0
    pic_aline list=1.6,0,1.6,0.1
    pic_text rn xy=1.4,1.0
    pic_circle list=1.6,0.3,1.6,0.5
end

picture gian
  pic_aline list=0.6,3,0.6,3.6
  pic_aline list=-0.6,3,-0.6,3.6
  pic_aline list=-0.6,5.4,-0.6,6
  pic_aline list=0.6,5.4,0.6,6
  pic_aline list=-2,8,2,8
  pic_aline list=0,4,0,5
  pic_aline list=0,8,0,9
  pic_aline list=-2,1,2,1
  pic_aline list=2,5,-2,5,0,8,2,5
  pic_aline list=0,0,0,1,2,4,-2,4,0,1
  pic_pin cathode b xy=0,0
  pic_pin anode b xy=0,9
end
picture pd_ballast
  pic_aline list=-0.4,1.8,0.4,1.8
  pic_aline list=0,2.4,0,2.6,0,3
  pic_aline list=1.4,2.8,1.4,-1.8,-1,-1.8,-1,2.8,1.4,2.8
  pic_aline list=0,0,0,0.3,0.4,0.6,-0.4,0.7,0.4,1,-0.4,1.2,0,1.4,0,1.6,0,1.8,0.4,2.4,-0.4,2.4,0,1.8
  pic_aline list=0,-2,0,-1.6,0.4,-1.4,-0.4,-1.2,0.4,-1,-0.4,-0.8,0,-0.6,0,0,2,0
  pic_pin sup1 b xy=0,3
  pic_pin pwr b xy=0,-2
  pic_pin mid b xy=2,0
end
picture state8
  pic_geom circle list=2,3,2,0
  pic_pin i1 i xy=2,6
  pic_pin o4 o xy=5,3
  pic_pin o8 o xy=2,0
  pic_pin o12 o xy=-1,3
  pic_pin o14 o xy=0,5
  pic_pin o10 o xy=0,1
  pic_pin o11 o xy=-1,2
  pic_pin o6 o xy=4,1
  pic_pin o7 o xy=3,0
  pic_pin o5 o xy=5,2
  pic_pin o3 o xy=5,4
  pic_pin o2 o xy=4,5
  pic_pin o1 o xy=3,5
  pic_pin o15 o xy=0,5
  pic_pin o13 o xy=-1,4
  pic_pin o9 o xy=0,0
end


schematic opening
inst corner_logo cr0 xy=-4.557265,-17.990503 rot=r90
inst corner_logo cr1 xy=56.865324,30.056947 rot=r270
inst cmos cmos_0 xy=14.821728,6.027391 rot=r90
inst input input_0 xy=0.149668,13.801899
inst vcc vcc_1 xy=5.644065,5.681861 rot=r180
inst node node_2 xy=1.122127,18.566952
inst inv inv1 xy=24.667806,10.777968
inst node node_0 xy=5.546819,13.369801
inst nand2 nand2_0 xy=24.080433,6.822802
inst gnd gnd_1 xy=5.455081,22.262298 rot=fr180
inst node node_1 xy=0.490028,9.863438
inst nmos nmos_0 xy=5.487522,20.761788 rot=fr270
inst nand2 nd2 xy=23.833808,15.340361
inst nor3 nor3_0 xy=24.000167,2.545893
inst pmos pmos_0 xy=5.575278,7.838383 rot=r90
inst inout inout_0 xy=14.931054,3.202089 rot=r90
inst output output_0 xy=7.297246,13.450522
inst gnd gnd_0 xy=14.681071,11.606034 rot=r180
geom text greenblat@mac.com|+972-54-4927322 list=-3.0,-11.0
geom text examples|of|drawing|with|some|instances list=-3.0,-9.0
geom text for|basics,|type|help|in|terminal list=-3.0,-13.0
wire wire0 vcc_1 pmos_0.i list=5.644065,5.681861,5.575278,7.838383
wire wire1 node_2 input_0 list=1.122127,18.566952,0.149668,13.801899
wire wire2 input_0 node_1 list=0.149668,13.801899,0.490028,9.863438
wire wire3 node_0 nmos_0.o list=5.546819,13.369801,5.487522,16.761788
wire wire4 inout_0 cmos_0.i list=14.931054,3.202089,14.821728,6.027391
wire wire5 node_1 pmos_0.g list=0.490028,9.863438,3.575278,9.838383
wire wire6 cmos_0.c nand2_0.i2 list=16.821728,8.027391,24.080433,7.822802
wire wire7 node_2 nmos_0.g list=1.122127,18.566952,3.487522,18.761788
wire wire8 gnd_1 nmos_0.i list=5.455081,22.262298,5.487522,20.761788
wire wire9 node_0 pmos_0.o list=5.546819,13.369801,5.575278,11.838383
wire wire10 cmos_0.o gnd_0 list=14.821728,10.027391,14.681071,11.606034
wire wire11 node_0 output_0 list=5.546819,13.369801,7.297246,13.450522
param input_0 name inx xy=-4.689649,13.316619
param output_0 name outx xy=10.102754,12.981766
param pmos_0 size 10/0.25 xy=5.018424,9.335043
end
picture flop
pic_pin q o xy=3.0,1.0
pic_pin ck i xy=1.5,2.5
pic_pin d i xy=0.0,1.0
pic_aline list=0.59,1.01,0.59,1.90
pic_aline list=0.59,1.90,1.45,1.90
pic_aline list=2.37,1.90,1.45,1.90
pic_aline list=2.37,1.90,2.37,0.98
pic_aline list=2.37,0.98,2.37,0.00
pic_aline list=2.37,0.00,0.59,0.00
pic_aline list=0.59,0.00,0.59,1.01
pic_aline list=1.45,2.53,1.45,1.90
pic_aline list=3.00,0.98,2.37,0.98
pic_aline list=0.00,1.01,0.59,1.01
pic_text d xy=0.8,0.7
pic_text q xy=1.9,0.7
pic_text ck xy=1.1,1.3
end
picture less
pic_pin o1 o xy=2.0,0.7
pic_pin i1 i xy=0.0,1.1
pic_pin i2 i xy=0.0,0.3
pic_aline list=2.00,0.67,1.49,0.67
pic_aline list=0.02,1.13,0.29,1.13
pic_aline list=0.00,0.31,0.31,0.31
pic_aline list=0.31,0.31,0.19,0.67
pic_aline list=0.29,1.13,0.19,0.67
pic_aline list=0.29,1.13,0.67,1.42
pic_aline list=0.67,1.42,1.20,1.42
pic_aline list=1.20,1.42,1.45,1.06
pic_aline list=1.45,1.06,1.49,0.67
pic_aline list=1.49,0.67,1.33,0.17
pic_aline list=1.33,0.17,0.72,0.00
pic_aline list=0.72,0.00,0.31,0.31
pic_aline list=1.01,0.55,0.65,0.82
pic_aline list=1.08,1.11,0.65,0.82
end
picture more
pic_pin o1 o xy=2.0,0.7
pic_pin i1 i xy=0.0,1.1
pic_pin i2 i xy=0.0,0.3
pic_aline list=2.00,0.67,1.49,0.67
pic_aline list=0.02,1.13,0.29,1.13
pic_aline list=0.00,0.31,0.31,0.31
pic_aline list=0.31,0.31,0.19,0.67
pic_aline list=0.29,1.13,0.19,0.67
pic_aline list=0.29,1.13,0.67,1.42
pic_aline list=0.67,1.42,1.20,1.42
pic_aline list=1.20,1.42,1.45,1.06
pic_aline list=1.45,1.06,1.49,0.67
pic_aline list=1.49,0.67,1.33,0.17
pic_aline list=1.33,0.17,0.72,0.00
pic_aline list=0.72,0.00,0.31,0.31
pic_aline list=0.65,0.51,1.04,0.75
pic_aline list=0.75,1.11,1.04,0.75
end
picture multififo_w1_r2
pic_aline list=0.5,0,0.5,5.0,5.2,5.0,5.2,0,0.5,0
pic_line list=0,1.0,0.5,0
pic_pin clk i xy=0,1.0
pic_text clk xy=0.6,1.0
pic_line list=0,2.0,0.5,0
pic_pin din i xy=0,2.0
pic_text din xy=0.6,2.0
pic_line list=0,3.0,0.5,0
pic_pin reads i xy=0,3.0
pic_text reads xy=0.6,3.0
pic_line list=0,4.0,0.5,0
pic_pin writes i xy=0,4.0
pic_text writes xy=0.6,4.0
pic_line list=5.2,1.5,0.5,0
pic_pin count i xy=5.7,1.5
pic_text count xy=5.2,1.5 align=right
pic_line list=5.2,2.5,0.5,0
pic_pin dout i xy=5.7,2.5
pic_text dout xy=5.2,2.5 align=right
pic_line list=5.2,3.5,0.5,0
pic_pin frees i xy=5.7,3.5
pic_text frees xy=5.2,3.5 align=right
pic_text multififo_w1_r2 xy=0.5,5.2
end
picture syncfifo
pic_aline list=0.5,0,0.5,5.0,4.5,5.0,4.5,0,0.5,0
pic_line list=0,1.0,0.5,0
pic_pin clk i xy=0,1.0
pic_text clk xy=0.6,1.0
pic_line list=0,2.0,0.5,0
pic_pin din i xy=0,2.0
pic_text din xy=0.6,2.0
pic_line list=0,3.0,0.5,0
pic_pin readout i xy=0,3.0
pic_text readout xy=0.6,3.0
pic_line list=0,4.0,0.5,0
pic_pin vldin i xy=0,4.0
pic_text vldin xy=0.6,4.0
pic_line list=4.5,2.0,0.5,0
pic_pin dout i xy=5.0,2.0
pic_text dout xy=4.5,2.0 align=right
pic_line list=4.5,3.0,0.5,0
pic_pin empty i xy=5.0,3.0
pic_text empty xy=4.5,3.0 align=right
pic_text syncfifo xy=0.5,5.2
end

'''

