from pydantic import BaseModel


class NetworkTrafficInput(BaseModel):

    Destination_Port: float

    Flow_Duration: float

    Total_Fwd_Packets: float

    Total_Backward_Packets: float

    Total_Length_of_Fwd_Packets: float

    Total_Length_of_Bwd_Packets: float

    Fwd_Packet_Length_Max: float

    Bwd_Packet_Length_Max: float

    Packet_Length_Mean: float

    Packet_Length_Std: float

    Average_Packet_Size: float

    Bwd_Packet_Length_Std: float

    Init_Win_bytes_forward: float

    Init_Win_bytes_backward: float