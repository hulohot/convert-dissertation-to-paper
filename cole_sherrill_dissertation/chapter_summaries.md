# Chapter Summaries

## 1. Introduction
The introduction discusses the current state of digital integrated circuit (IC) design and its challenges. Key points include:

- Industry standard involves using Hardware Description Languages (HDL) like Verilog/VHDL for behavioral design
- Current design flow: behavioral description → logical synthesis → physical implementation
- Electronic Design Automation (EDA) tools are crucial for modern multi-GHz, multi-core designs
- Synchronous design methodology limitations:
  - High peak power demand
  - Increased noise
  - Greater electromagnetic interference
  - Performance bottlenecked by worst-case scenarios
- Introduces MTNCL (Multi-Threshold NULL Convention Logic) as an asynchronous alternative
- Research focus: First design flow for MTNCL using commercial EDA tools

## 2. BACKGROUND

### Circuit Synthesis Evolution
- Historical transition from structural to behavioral design
- Advantages of modern synthesis:
  - Faster design cycles
  - Greater optimization opportunities
  - Automated architecture selection
  - Register retiming capabilities
- Impact of deep submicron technologies on synthesis
- Physical synthesis importance for routing delay consideration

### Placement and Routing
- Timing constraints crucial for implementation
- Multiple optimization strategies:
  - Cell placement optimization
  - Metal layer selection
  - Coupling capacitance management
  - Gate sizing and buffering
- Power and area optimization after timing closure

### NULL Convention Logic (NCL)
- Quasi-delay-insensitive asynchronous design
- Multi-rail logic implementation
- 27 fundamental threshold gates
- Key characteristics:
  - Input-completeness requirement
  - Observability requirements
  - Hysteresis in threshold gates
- Pipeline structure with delay-insensitive registers

### Multi-Threshold NULL Convention Logic (MTNCL)
- Integration with MTCMOS power gating
- Architectural improvements over NCL:
  - Sleep transistors for NULL generation
  - Simplified gate structure
  - No hysteresis requirement
  - Removal of input-completeness requirement
- Pipeline structure and completion detection
- Sleep tree implementation challenges
- Performance determined by DATA wave propagation

### MTNCL Timing Sensitivity
- Four critical timing assumptions:
  1. DATA completion race condition
  2. DATA handshaking race condition
  3. NULL wave generation timing
  4. NULL handshaking race condition
- Impact of modern process nodes on timing
- Mitigation strategies and challenges

### Synthesis Approaches
- NCL synthesis challenges:
  - Commercial EDA limitations
  - Liberty model generation
  - Image library requirements
- MTNCL synthesis developments:
  - Multiple proposed flows
  - Common challenges in sleep network implementation
  - Limitations in existing approaches
  - Need for timing constraint support

## 3. MTNCL RTL-TO-GDS FLOW
Details the implementation flow for MTNCL circuits:

### Library Preparation
- Custom cell libraries development required
- Modifications needed for MTNCL gates:
  - Sleep pin handling
  - Liberty model adjustments
  - Timing arc optimizations

### Synthesis Flow
- 14-step process organized under top-level Makefile
- Takes standard behavioral synchronous RTL as input
- Three main phases:
  1. Single-rail Synthesis
  2. Dual-rail Expansion
  3. Dual-rail Synthesis
- Novel approach to completion detection synthesis
- Careful constraints required to maintain logical correctness 

## 4. EVALUATION SETUP
This chapter details the setup and methodology for evaluating MTNCL circuits:

### Commercial Synthesis Requirements
- Basic cell requirements for synthesis tools
- Challenges with inverter cells in MTNCL
- Solutions for handling negative unate cells
- Workarounds for synthesis tool limitations

### Timing Constraints
- Breaking combinational timing loops
- Four pairs of timing constraints for reliability:
  1. DATA completion race condition
  2. DATA handshaking race condition
  3. NULL completion timing
  4. NULL handshaking race condition
- Additional constraints for optimization
- Interface timing considerations

## 5. RESULTS AND ANALYSIS
Presents comprehensive analysis of implemented circuits:

### Circuit Implementations
- 64-bit Adders (RCA and CLA implementations)
- Montgomery Modular Multipliers
- AES-256 Cores

### Key Findings
- Comparison between structural and synthesized designs
- Performance analysis of low-power vs. high-performance implementations
- Detailed timing path analysis
- Cell composition and area utilization studies

### Notable Results for Low-Power Designs
- 30% throughput reduction in synthesized vs. structural low-power adders
- Sleep signal buffering differences:
  - Structural design: larger buffers, lower fanout
  - Synthesized design: smaller inverters, higher fanout
- Power consumption improvements:
  - 8.9% less active energy in synthesized design
  - 11.7% less leakage power
  - Only 1.9% area reduction
- Optimized design achievements:
  - 16% throughput improvement over synthesized
  - Similar active energy usage
  - 13.1% better Energy-Delay Product (EDP)

### Notable Results for High-Performance Designs
- Structural CLA achieves 1.25x throughput of synthesized design
- Logic depth comparison:
  - Structural: 14 MTNCL gates
  - Synthesized: 8 gates
- Synthesized design shows 125ps less delay in critical paths
- Trade-offs between performance and power consumption evident

### Detailed Timing Analysis
- NULL cycle time analysis reveals key performance differences:
  - Structural design: faster NULL cycle completion
  - Synthesized design: 125ps slower NULL cycle time
- Ki-to-output path differences:
  - Structural: ~168ps buffering delay
  - Synthesized: ~382ps buffering delay (2.3x longer)
- Performance variations due to:
  - Sleep signal buffering strategies
  - Transition time constraints
  - Routing and parasitic effects
  - Input interface delays

### Power and Area Analysis
- Synthesized high-performance design:
  - 19.2% larger area than structural
  - 9.3% less active energy per operation
  - 14.7% less idle power consumption
- Power efficiency achieved through:
  - Optimized cell selection
  - Better switching activity management
  - Improved completion detection paths

### Implementation Details
- Sleep tree implementation crucial for power and performance
- Timing constraints significantly impact design optimization
- Careful buffer sizing and distribution essential
- Completion detection optimization important for overall performance
- Race condition mitigation through proper timing closure essential

### Montgomery Modular Multiplier Results
#### Low-Power Design Achievements
- Significant improvements through synthesis flow and timing constraints:
  - 59.5% higher throughput
  - 28.6% less active energy
  - 42.9% less leakage power
  - 29.6% area reduction
  - 55.2% better Energy-Delay Product (EDP)

#### High-Performance Design Achievements
- Performance comparison of 4-stage implementations:
  - 39.5% throughput improvement in synthesized design
  - 5.4% less active energy consumption
  - 8.2% less leakage power
  - 32.2% EDP reduction
  - 10.6% area increase but with better utilization

#### Implementation Details
- Pipeline stage optimization:
  - Structural design: up to 5,478ps variation between stages
  - Synthesized design: only 1,210ps variation (78% reduction)
  - Worst stage delay reduced from 9,172ps to 4,503ps
- Cell utilization improvements:
  - 67% more cells in synthesized design
  - More efficient area usage with varied cell sizes
  - 55% more total wire length but better overall performance
- Architecture selection:
  - Structural: Fixed array multipliers and RCAs
  - Synthesized: Optimized architecture (likely Wallace tree adders)
  - Register retiming enabled for optimal pipeline balance

### AES-256 Implementation Results
#### Architecture and Design Considerations
- Complex sequential implementation with FSM
- Key differences between structural and synthesized designs:
  - Key expansion: 7-cycle vs. 115-cycle FSM (unrolled)
  - S-box implementation variations:
    - Lookup table for high-performance
    - Mathematical implementation for low-power
  - Manual intervention required for synthesis flow
  - Separate optimization of key expansion and round logic

#### Low-Power Design Results
- Performance metrics:
  - 15.7% throughput reduction in synthesized design
  - 22.7% less active energy consumption
  - 24.3% less leakage power
  - 8.4% better Energy-Delay Product
  - 15.4% area increase
- Implementation characteristics:
  - 27% more cell instances in synthesized design
  - More efficient cell selection for power optimization
  - Average-case performance benefits in structural design
  - Cycle time breakdown:
    - Key expansion: 7 iterations vs. 1 iteration
    - Round logic: 14 iterations in both designs
    - Different optimization strategies for timing paths

#### High-Performance Design Results
- Optimized vs. Synthesized comparison:
  - 65.1% throughput improvement
  - 16.7% increase in active energy
  - 26.0% increase in leakage power
  - 29.3% better Energy-Delay Product
  - 3.1% area increase
- Timing improvements:
  - Key expansion delay reduced by 46%
  - Round logic delay reduced by 42%
- Buffer delay analysis:
  - Synthesized design: 59-61% buffer delay
  - Optimized design: 18-39% buffer delay
  - More efficient timing path optimization

### Race Condition Analysis
- Critical timing hazards identified in high-performance designs
- DATA handshaking hazard observed in Montgomery multipliers
- Importance of timing closure for reliability:
  - Post-silicon issues difficult to resolve
  - Proper constraints essential for robust operation
  - Multiple ECO iterations required for some designs
  - PVT corner considerations crucial

## 6. CONCLUSIONS

### Summary
- First comprehensive design flow from synchronous RTL to optimized MTNCL implementations
- Novel timing constraints for reliability and optimization
- Demonstrated superior results compared to structural designs:
  - Up to 140% higher throughput for high-performance circuits
  - Up to 28.6% less active energy, 42.9% less static power, and 29.6% less area for low-power designs
- Previous MTNCL performance limitations may be due to design methodology rather than inherent limitations

### Key Pitfalls
- Initial synthesis flow challenges with Boolean vs. MTNCL cell libraries
- Issues with generic synthesis optimization causing circuit logic explosion
- Specific challenges with arithmetic circuit optimization
- Need for careful constraint management in complex designs

### Future Work
- Extend support for sequential designs and mixed logic types
- Improve cell library consistency between single-rail and dual-rail synthesis
- Optimize timing constraints for easier closure
- Automate constraint generation for complex designs
- Investigate better approaches for inverter handling
- Develop standards for constraint value selection 