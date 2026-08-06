import os

def generate_satellite_orbit(filename="orbit.svg"):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500" viewBox="0 0 500 500">
  <style>
    .ocean { fill: #0984e3; }
    .land { fill: #00b894; }
    .orbit-path { fill: none; stroke: #888888; stroke-width: 2; stroke-dasharray: 6 10; opacity: 0.4; }
    .panel { fill: #0984e3; stroke: #ffffff; stroke-width: 1.5; }
    .body { fill: #fdcb6e; stroke: #ffffff; stroke-width: 1.5; }
    .antenna { fill: none; stroke: #dfe6e9; stroke-width: 3; stroke-linecap: round; }
    .signal-down { stroke: #00cec9; stroke-width: 3; stroke-linecap: round; stroke-dasharray: 8 6; }
    .signal-up { stroke: #fd79a8; stroke-width: 3; stroke-linecap: round; stroke-dasharray: 8 6; }
  </style>

  <!-- Dimmed Orbital Trajectory -->
  <circle cx="250" cy="250" r="160" class="orbit-path" />

  <!-- Rotating Earth -->
  <clipPath id="globe-clip">
    <circle cx="250" cy="250" r="75" />
  </clipPath>
  
  <g clip-path="url(#globe-clip)">
    <!-- Deep Ocean Background -->
    <circle cx="250" cy="250" r="75" class="ocean" />
    
    <!-- Continents Panning Left to Simulate Rotation -->
    <g class="land">
      <animateTransform 
        attributeName="transform" 
        type="translate" 
        from="0 0" 
        to="-150 0" 
        dur="10s" 
        repeatCount="indefinite" 
      />
      
      <!-- Map Block 1 (Starts inside the globe) -->
      <path d="M 185 200 Q 200 180 215 200 T 215 240 T 195 280 T 175 250 Z" />
      <path d="M 230 190 Q 250 170 275 190 T 260 250 T 235 270 Z" />
      <path d="M 285 240 Q 305 230 315 250 T 295 280 Z" />
      
      <!-- Map Block 2 (Duplicate shifted +150px to loop seamlessly) -->
      <path d="M 335 200 Q 350 180 365 200 T 365 240 T 345 280 T 325 250 Z" />
      <path d="M 380 190 Q 400 170 425 190 T 410 250 T 385 270 Z" />
      <path d="M 435 240 Q 455 230 465 250 T 445 280 Z" />
    </g>
  </g>

  <!-- The Satellite and Signals -->
  <g>
    <!-- Rotate the entire satellite group around the Earth (12 seconds per orbit) -->
    <animateTransform 
        attributeName="transform" 
        type="rotate" 
        from="0 250 250" 
        to="360 250 250" 
        dur="12s" 
        repeatCount="indefinite" 
    />
    
    <!-- Satellite Build (Left side always points toward Earth) -->
    <line x1="410" y1="215" x2="410" y2="285" stroke="#b2bec3" stroke-width="3" />
    <rect x="395" y="200" width="30" height="25" rx="2" class="panel" />
    <rect x="395" y="275" width="30" height="25" rx="2" class="panel" />
    <rect x="400" y="240" width="20" height="20" rx="4" class="body" />
    
    <!-- Antenna facing Earth -->
    <line x1="400" y1="250" x2="385" y2="250" stroke="#b2bec3" stroke-width="3" />
    <path d="M 385 235 Q 370 250 385 265" class="antenna" />
    <circle cx="380" cy="250" r="3" fill="#d63031" />

    <!-- Signal 1: Downlink (Satellite to Earth - Cyan) -->
    <!-- Triggers between 2.4s and 4.8s of the orbit loop -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 0; 1; 0; 0" keyTimes="0; 0.2; 0.3; 0.4; 1" dur="12s" repeatCount="indefinite" />
      <line x1="370" y1="250" x2="330" y2="250" class="signal-down">
        <animate attributeName="stroke-dashoffset" from="14" to="0" dur="0.4s" repeatCount="indefinite" />
      </line>
    </g>

    <!-- Signal 2: Uplink (Earth to Satellite - Pink) -->
    <!-- Triggers between 7.2s and 9.6s of the orbit loop -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 0; 0; 1; 0; 0" keyTimes="0; 0.6; 0.7; 0.8; 0.9; 1" dur="12s" repeatCount="indefinite" />
      <line x1="330" y1="250" x2="370" y2="250" class="signal-up">
        <animate attributeName="stroke-dashoffset" from="0" to="14" dur="0.4s" repeatCount="indefinite" />
      </line>
    </g>
  </g>
</svg>"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    print(f"Successfully generated {filename}!")

if __name__ == "__main__":
    generate_satellite_orbit()
