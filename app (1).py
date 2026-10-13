import streamlit as st

st.set_page_config(page_title="LiftLogic", page_icon="🛗")

st.title("🛗 LiftLogic")
st.subheader("Smart Elevator Control and Simulation System")

st.write("A digital logic based elevator simulator")

if "floor" not in st.session_state:
    st.session_state.floor = 0

if "target" not in st.session_state:
    st.session_state.target = 0

if "door_open" not in st.session_state:
    st.session_state.door_open = True

if "moving" not in st.session_state:
    st.session_state.moving = False

st.markdown("### Elevator Status")
st.metric("Current Floor", st.session_state.floor)
st.write("Door:", "OPEN" if st.session_state.door_open else "CLOSED")

st.markdown("### Select Destination")
target = st.selectbox("Choose floor", [0, 1, 2, 3, 4],
                      index=st.session_state.target)

if st.button("Request Floor"):
    st.session_state.target = target
    st.session_state.door_open = False
    st.session_state.moving = (
        target != st.session_state.floor
    )

if st.button("Move One Floor"):
    if st.session_state.door_open:
        st.warning("Close the door before moving.")
    elif st.session_state.floor < st.session_state.target:
        st.session_state.floor += 1
    elif st.session_state.floor > st.session_state.target:
        st.session_state.floor -= 1

    if st.session_state.floor == st.session_state.target:
        st.session_state.moving = False
        st.session_state.door_open = True
        st.success("Destination reached!")

st.markdown("### Floor Display")
for f in range(4, -1, -1):
    if f == st.session_state.floor:
        st.success(f"▶ FLOOR {f}  — ELEVATOR")
    else:
        st.write(f"　 FLOOR {f}")

st.markdown("### Digital Logic Status")

up = (
    st.session_state.target > st.session_state.floor
    and not st.session_state.door_open
)
down = (
    st.session_state.target < st.session_state.floor
    and not st.session_state.door_open
)
stop = (
    st.session_state.target == st.session_state.floor
    or st.session_state.door_open
)

st.write("Motor UP:", int(up))
st.write("Motor DOWN:", int(down))
st.write("Motor STOP:", int(stop))
st.caption("Educational simulation only — not for real elevator control.")
