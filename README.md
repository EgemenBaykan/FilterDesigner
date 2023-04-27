<h1><b>Filter Designer</b></h1>

<p>Filter Designer is a console program that designs 4 basic filters for given inputs. It is written in Python and Jupyter Notebook will be available soon. It is not recommended to use frequencies above 200-300 MHz since wavelength decreases in lumped element model filters. Use distributed element model for higher frequencies.</p>

<p>Filters are circuits that can pass or stop given frequencies or frequency bands. Passive filters contain passive elements unlike active filters. These elements are resistors, capacitors and inductors. Resistor is not a good practice in RF circuits. Therefore inductors are used instead of resistors since they boost the current.</p>

<p>In practice, passive filters are designed by using <b>Normalized Filter Coefficient Tables</b>. Filter order and characteristic are determined by performance requirements. This is, usually, done by providing attenuation on unwanted frequency components. Bode plots are used to analyze frequency response of RF circuits such as filters and magnitude is in <b>Decibel (dB)</b> scale.</p>

<h3><b>Program Inputs</b></h3>

<p> Basically there are 5 types of program inputs. These inputs are explained as follow:</p>

<ol>
    <li> <b>Filter Type:</b> </li>
    <ul>
        <li><b>LPF:</b> Defines Low Pass Filter.</li>
        <li><b>HPF:</b> Defines High Pass Filter.</li>
        <li><b>BPF:</b> Defines Band Pass Filter.</li>
        <li><b>BSF:</b> Defines Band Stop Filter.</li>
    </ul>
    <li> <b>Cutoff Frequency:</b> Defines -3dB point(s) of the filter. Low and high cutoff frequencies are given as inputs for Bandpass Filter or Bandstop Filter. Scientific notation is used for cutoff frequencies in Hz.</li>
    <li> <b>Filter Characteristic:</b> Defines filter characteristics to calculate zeros and poles. Only <b>Butterworth</b> and <b>Chebyshev</b> filters are available. Bessel response will be implemented in further updates.</li>
    <li> <b>Impedance:</b> Filter impedance. Typically 50 ohms. It is considered as source impedance is equal to load impedance in calculations. For impedance matching networks see Impedance Matching calculation tool repo.</li>
    <li> <b>Filter Order:</b> Filter order directly effects Transfer Function of the circuit in analysis. It's also can be obtained by number of delay elements of a circuit as seen in Finite Impulse Response (FIR) filter designs. </li>
</ol>


<h3><b>Program Outputs</b></h3>

<p> Filter coefficients, capacitor and inductor values are given as outputs at then end of program. Scientific notation is used for values of capacitors and inductors. All arrays are printed to console.
</p>


<h2> How to design a filter using Filter Designer?</h2>

<p> <b>It's strictly recommended to simulate the circuit by obtained values in filter topologies.</b> Run the program in the console and make an AC Analysis in <b>LTSpice</b> in order to analyze <b>Frequency Response</b> for obtained circuit. All the tests are done by simulation and few of obtained circuits are built on PCB's. Use a <b>Vector Network Analyzer (VNA)</b> for measurements on real PCB's. <b>S21</b> parameters on VNA must be matched with simulations.</p>
<p> Some of the simulations and measurements are given in following images.</p>

<p> Circuit topologies for High Pass and Low Pass Filters can be seen in image. Each circuit is labeled by its type, characteristic and cutoff frequency.</p>
<img src="Simulation.png" alt="Filter topology used in simulation." style="width:300px;height:400px;">
<p> Simulation outputs can be observed as given for given generated circuits. Butterworth Low Pass Filter output is plotted in blue color. Butterworth and Chebyshev High Pass Filters are plotted in red and cyan colors.</p>
<img src="Simulation_Outputs.png" alt="Frequency Response in simulation." style="width:400px;height:300px;">


<h2> References </h2>

<ol>
    <li> WINDER, S., Analog and Digital Filter Design.</li>
</ol>


