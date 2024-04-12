//ATF: 1502
//OPT: -device PLCC44
//OPT: -strategy pin_keep on
//PIN: CHIP "top" ASSIGNED TO PLCC44
//PIN: CLK : 43
//PIN: O : 21
module top(input CLK, output O);
  TFF tff(.CLK(CLK), .T(1'b1), .Q(O));
endmodule
