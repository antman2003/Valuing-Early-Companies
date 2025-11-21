"""
Illustrative plots for valuing high-growth, early-stage companies.

Generates:
1. A profile of free cash flow vs. discounted free cash flow over time.
2. A distribution of discounted exit values in a VC-style investment.

Figures are saved to the top-level `figures/` directory as:
- early_stage_dcf_profile.png
- exit_value_distribution.png
"""

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def ensure_figures_dir() -> str:
    """Ensure the figures directory exists and return its path."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    figures_dir = os.path.join(root, "figures")
    os.makedirs(figures_dir, exist_ok=True)
    return figures_dir


def plot_dcf_profile(figures_dir: str) -> None:
    """
    Plot free cash flow and discounted free cash flow for a stylised early-stage company.

    The example assumes:
    - Negative free cash flow for the first few years due to heavy reinvestment.
    - Rapid improvement as the business scales and unit economics turn positive.
    - A high discount rate typical of venture-style opportunities.
    """
    # Years 0–10 (0 is "today")
    years = np.arange(0, 11)

    # Hypothetical free cash flows in USD millions.
    # Negative in early years, then strongly positive as the business scales.
    fcf = np.array(
        [-5.0, -4.0, -2.0, 0.0, 3.0, 7.0, 12.0, 18.0, 22.0, 25.0, 27.0]
    )

    # Venture-style required return (e.g. 25%).
    r = 0.25
    discount_factors = 1.0 / (1.0 + r) ** years
    pv_fcf = fcf * discount_factors

    df = pd.DataFrame(
        {
            "Year": years,
            "Free cash flow (USD m)": fcf,
            "Discounted FCF (USD m)": pv_fcf,
        }
    )

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.lineplot(
        data=df,
        x="Year",
        y="Free cash flow (USD m)",
        marker="o",
        label="Free cash flow",
    )
    sns.lineplot(
        data=df,
        x="Year",
        y="Discounted FCF (USD m)",
        marker="o",
        label="Discounted free cash flow",
    )
    plt.axhline(0.0, color="black", linewidth=0.8)
    plt.title("Early-Stage Company: Free Cash Flow vs. Discounted Free Cash Flow")
    plt.xlabel("Year")
    plt.ylabel("USD millions")
    plt.legend()
    plt.tight_layout()

    output_path = os.path.join(figures_dir, "early_stage_dcf_profile.png")
    plt.savefig(output_path, dpi=300)
    plt.close()


def plot_exit_value_distribution(figures_dir: str) -> None:
    """
    Plot a distribution of discounted exit values for a VC-style investment.

    Assumptions:
    - A 7-year horizon.
    - 40% outright failure (zero equity value).
    - Remaining outcomes follow a lognormal distribution of exit equity values.
    - Required return of 35% per year.
    """
    np.random.seed(42)

    n_sims = 10_000

    # Lognormal exit equity values in USD millions for surviving companies.
    # Parameters chosen to produce a wide, skewed distribution centred around ~100m.
    mu = np.log(100.0) - 0.5 * 0.8**2
    sigma = 0.8
    exit_values = np.random.lognormal(mean=mu, sigma=sigma, size=n_sims)

    # Introduce a probability of total failure (zero exit value).
    failure_prob = 0.40
    failure_draws = np.random.rand(n_sims)
    exit_values[failure_draws < failure_prob] = 0.0

    # Discount back 7 years at a high required return.
    R = 0.35
    T = 7
    discount_factor = 1.0 / (1.0 + R) ** T
    pv_exit_values = exit_values * discount_factor

    df = pd.DataFrame({"Discounted exit value (USD m)": pv_exit_values})

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.histplot(
        data=df,
        x="Discounted exit value (USD m)",
        bins=60,
        kde=False,
        color="steelblue",
    )
    plt.title(
        "Distribution of Discounted Exit Values\n"
        "VC-style Investment in a High-Growth Early-Stage Company"
    )
    plt.xlabel("Discounted exit equity value (USD millions)")
    plt.ylabel("Simulated frequency")
    plt.xlim(left=0.0)
    plt.tight_layout()

    output_path = os.path.join(figures_dir, "exit_value_distribution.png")
    plt.savefig(output_path, dpi=300)
    plt.close()


def main() -> None:
    figures_dir = ensure_figures_dir()
    plot_dcf_profile(figures_dir)
    plot_exit_value_distribution(figures_dir)
    print(f"Figures saved in: {figures_dir}")


if __name__ == "__main__":
    main()


